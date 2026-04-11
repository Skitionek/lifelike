import {
  Injectable,
  Injector,
} from '@angular/core';
import {
  NavigationExtras,
  Router,
  UrlTree,
} from '@angular/router';
import { moveItemInArray, transferArrayItem } from '@angular/cdk/drag-drop';

import { BehaviorSubject } from 'rxjs';
import { cloneDeep } from 'lodash-es';

import { ModuleProperties } from './modules';
import {
  TabData,
  WorkspaceSessionLoader,
  WorkspaceSessionService,
} from './services/workspace-session.service';

export interface TabDefaults {
  title: string;
  fontAwesomeIcon: string;
}

/**
 * Represents a tab with a title and URL.
 */
export class Tab {
  workspaceManager: WorkspaceManager;
  url: string;
  defaultsSet = false;
  title = 'New Tab';
  fontAwesomeIcon: string = null;
  badge: string = null;
  loading = false;

  pendingProperties: ModuleProperties | undefined;

  get absoluteUrl(): string {
    return new URL(this.url.replace(/^\/+/, '/'), new URL(window.location.href)).href;
  }

  queuePropertyChange(properties: ModuleProperties) {
    this.pendingProperties = cloneDeep(properties);
  }

  applyPendingChanges() {
    if (this.pendingProperties) {
      this.title = this.pendingProperties.title;
      this.fontAwesomeIcon = this.pendingProperties.fontAwesomeIcon;
      this.badge = this.pendingProperties.badge;
      this.loading = !!this.pendingProperties.loading;
      this.pendingProperties = null;
      if (this.workspaceManager) {
        this.workspaceManager.save();
      }
    }
  }

  /** @deprecated No longer used; router outlets manage component lifecycle. */
  getComponent(): any | undefined {
    return null;
  }
}

/**
 * Represents a pane that has a collection of tabs.
 */
export class Pane {
  size: number | undefined;
  readonly tabs: Tab[] = [];
  readonly activeTabHistory: Set<Tab> = new Set();

  constructor(
    readonly id: string,
    private readonly workspaceManager: WorkspaceManager,
  ) {}

  applyPendingChanges() {
    for (const tab of this.tabs) {
      tab.applyPendingChanges();
    }
  }

  get activeTab(): Tab | undefined {
    let active: Tab = null;
    for (const tab of this.activeTabHistory.values()) {
      active = tab;
    }
    return active;
  }

  set activeTab(tab: Tab) {
    if (tab != null) {
      this.activeTabHistory.delete(tab);
      this.activeTabHistory.add(tab);
    }
  }

  getActiveTabOrCreate(): Tab {
    const tab = this.activeTab;
    if (tab) {
      return tab;
    }
    if (this.tabs.length) {
      this.activeTab = this.tabs[0];
      return this.activeTab;
    }
    return this.createTab();
  }

  createTab(): Tab {
    const tab = new Tab();
    tab.workspaceManager = this.workspaceManager;
    this.tabs.push(tab);
    this.activeTab = tab;
    return tab;
  }

  deleteTab(tab: Tab): boolean {
    for (let i = 0; i < this.tabs.length; i++) {
      if (this.tabs[i] === tab) {
        this.tabs.splice(i, 1);
        this.activeTabHistory.delete(tab);
        return true;
      }
    }
    return false;
  }

  deleteActiveTab(): boolean {
    const activeTab = this.activeTab;
    if (activeTab) {
      return this.deleteTab(activeTab);
    }
    return false;
  }

  handleTabMoveFrom(tab: Tab) {
    this.activeTabHistory.delete(tab);
  }

  handleTabMoveTo(tab: Tab) {
    this.activeTabHistory.add(tab);
  }

  destroy() {
    for (const tab of this.tabs.slice()) {
      this.deleteTab(tab);
    }
  }
}

/**
 * Manages a set of panes.
 */
export class PaneManager {
  panes: Pane[] = [];

  constructor(private readonly workspaceManager: WorkspaceManager) {}

  create(id: string): Pane {
    for (const existingPane of this.panes) {
      if (existingPane.id === id) {
        throw new Error(`pane ${existingPane.id} already created`);
      }
    }
    const pane = new Pane(id, this.workspaceManager);
    this.panes.push(pane);
    return pane;
  }

  get(id: string): Pane | undefined {
    for (const pane of this.panes) {
      if (pane.id === id) {
        return pane;
      }
    }
    return null;
  }

  getOrCreate(id: string): Pane {
    const pane = this.get(id);
    if (pane) {
      return pane;
    }
    return this.create(id);
  }

  getFirstOrCreate() {
    const it = this.panes.values().next();
    return !it.done ? it.value : this.create('left');
  }

  delete(pane: Pane): boolean {
    for (let i = 0; i < this.panes.length; i++) {
      if (this.panes[i] === pane) {
        this.panes.splice(i, 1);
        pane.destroy();
        return true;
      }
    }
    return false;
  }

  clear() {
    for (const pane of this.panes.slice()) {
      this.delete(pane);
    }
  }

  *allTabs(): IterableIterator<{ pane: Pane; tab: Tab }> {
    for (const pane of this.panes) {
      for (const tab of pane.tabs) {
        yield { pane, tab };
      }
    }
  }

  applyPendingChanges() {
    for (const pane of this.panes) {
      pane.applyPendingChanges();
    }
  }
}

@Injectable({
  providedIn: 'root',
})
export class WorkspaceManager {
  panes: PaneManager;
  readonly workspaceUrl = '/workspaces/local';
  focusedPane: Pane | undefined;
  panes$ = new BehaviorSubject<Pane[]>([]);
  private loaded = false;

  constructor(
    private readonly router: Router,
    private readonly sessionService: WorkspaceSessionService,
  ) {
    this.panes = new PaneManager(this);
    this.emitEvents();
  }

  isWithinWorkspace() {
    return this.router.url.startsWith(this.workspaceUrl);
  }

  moveTab(from: Pane, fromIndex: number, to: Pane, toIndex: number) {
    if (from === to) {
      moveItemInArray(from.tabs, fromIndex, toIndex);
    } else {
      const tab = from.tabs[fromIndex];
      transferArrayItem(from.tabs, to.tabs, fromIndex, toIndex);
      from.handleTabMoveFrom(tab);
      to.handleTabMoveTo(tab);
    }
    this.save();
    this.emitEvents();
  }

  openTabByUrl(
    pane: Pane | string,
    url: string | UrlTree,
    extras?: NavigationExtras & WorkspaceNavigationExtras,
    tabDefaults?: TabDefaults,
  ): Promise<boolean> {
    if (typeof pane === 'string') {
      pane = this.panes.getOrCreate(pane);
    }
    this.focusedPane = pane;
    const tab = pane.createTab();
    tab.url = url.toString();
    if (tabDefaults) {
      tab.title = tabDefaults.title;
      tab.fontAwesomeIcon = tabDefaults.fontAwesomeIcon;
      tab.defaultsSet = true;
    }
    return this.navigateByUrl({ url, extras });
  }

  navigateByUrl(navigationData: NavigationData): Promise<boolean> {
    const extras = navigationData.extras || {};
    const urlStr = navigationData.url.toString();
    const withinWorkspace = this.isWithinWorkspace();

    if (withinWorkspace) {
      let targetPane = this.focusedPane || this.panes.getFirstOrCreate();

      if (extras.newTab) {
        if (extras.sideBySide) {
          let sideBySidePane: Pane = null;
          for (const otherPane of this.panes.panes) {
            if (targetPane.id !== otherPane.id) {
              sideBySidePane = otherPane;
              break;
            }
          }
          if (sideBySidePane == null) {
            if (targetPane.id === 'left') {
              targetPane = this.panes.create('right');
            } else {
              targetPane = this.panes.create('left');
            }
          } else {
            targetPane = sideBySidePane;
          }
        }

        if (extras.preferPane) {
          const preferredPane = this.panes.get(extras.preferPane);
          if (preferredPane) {
            targetPane = preferredPane;
          }
        }

        if (extras.matchExistingTab != null) {
          let foundTab = false;
          for (const tab of targetPane.tabs) {
            if (tab.url && tab.url.match(extras.matchExistingTab)) {
              targetPane.activeTab = tab;
              foundTab = true;
              break;
            }
          }
          if (!foundTab) {
            targetPane.createTab();
          }
        } else {
          targetPane.createTab();
        }

        this.focusedPane = targetPane;
      }

      const segments = urlStr.replace(/^\//, '').split('/');
      const activeTab = targetPane.activeTab;
      if (activeTab) {
        activeTab.url = urlStr;
      }
      this.save();
      this.emitEvents();
      return this.router.navigate([{ outlets: { [targetPane.id]: segments } }]);
    } else if (extras.forceWorkbench) {
      return this.router.navigateByUrl(this.workspaceUrl).then(() => {
        return this.navigateByUrl(navigationData);
      });
    } else {
      return this.router.navigateByUrl(navigationData.url, extras);
    }
  }

  navigateByUrls(navigationData: NavigationData[]): Promise<boolean> {
    return new Promise((accept, reject) => {
      navigationData.forEach(navData => {
        const extras = navData.extras || {};
        setTimeout(() => {
          this.navigateByUrl({ url: navData.url, extras }).then(accept, reject);
        }, 10);
      });
    });
  }

  navigate(
    commands: any[],
    extras: NavigationExtras & WorkspaceNavigationExtras = { skipLocationChange: false },
  ): Promise<boolean> {
    return this.navigateByUrl({ url: this.router.createUrlTree(commands, extras), extras });
  }

  emitEvents(): void {
    this.panes$.next(this.buildPanesSnapshot());
  }

  initialLoad() {
    if (!this.loaded) {
      this.loaded = true;
      this.load();
    }
  }

  load() {
    const parent = this;
    const tasks: Array<() => void> = [];

    if (
      this.sessionService.load(
        new (class implements WorkspaceSessionLoader {
          createPane(id: string, options: { size: number | undefined }): void {
            tasks.push(() => {
              const pane = parent.panes.create(id);
              pane.size = options.size;
            });
          }

          loadTab(id: string, data: TabData): void {
            tasks.push(() => {
              parent.openTabByUrl(id, data.url, null, {
                title: data.title,
                fontAwesomeIcon: data.fontAwesomeIcon,
              });
            });
          }

          setPaneActiveTabHistory(id: string, indices: number[]): void {
            tasks.push(() => {
              const pane = parent.panes.get(id);
              const activeTabHistory = pane.activeTabHistory;
              activeTabHistory.clear();
              indices.forEach(index => {
                activeTabHistory.add(pane.tabs[index]);
              });
            });
          }
        })(),
      )
    ) {
      this.panes.clear();
      tasks.reduce((previousTask, task) => {
        return previousTask.then(task);
      }, Promise.resolve());
    } else {
      const leftPane = this.panes.create('left');
      this.panes.create('right');
      this.openTabByUrl(leftPane, '/projects');
    }
  }

  save() {
    this.sessionService.save(this.panes.panes);
  }

  shouldConfirmUnload(): { pane: Pane; tab: Tab } | undefined {
    for (const { pane, tab } of this.panes.allTabs()) {
      if (this.shouldConfirmTabUnload(tab)) {
        return { pane, tab };
      }
    }
    return null;
  }

  shouldConfirmTabUnload(tab: Tab) {
    return false;
  }

  applyPendingChanges() {
    this.panes.applyPendingChanges();
  }

  private buildPanesSnapshot(): Pane[] {
    return this.panes.panes;
  }
}

export interface WorkspaceNavigationExtras {
  preferPane?: string;
  preferStartupPane?: string;
  newTab?: boolean;
  sideBySide?: boolean;
  matchExistingTab?: string | RegExp;
  shouldReplaceTab?: (component: any) => boolean;
  forceWorkbench?: boolean;
  openParentFirst?: boolean;
  parentAddress?: UrlTree;
}

export interface NavigationData {
  url: string | UrlTree;
  extras?: NavigationExtras & WorkspaceNavigationExtras;
}
