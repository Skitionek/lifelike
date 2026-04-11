import {
  Component,
  HostListener,
  OnInit,
  ViewEncapsulation,
} from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { map, Observable, switchMap } from 'rxjs';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { CdkDragDrop } from '@angular/cdk/drag-drop';

import { OutletsMap } from 'app/shared/route-with-dynamic-outlets';
import { Pane, Tab, WorkspaceManager } from 'app/shared/workspace-manager';
import { CopyLinkDialogComponent } from 'app/shared/components/dialog/copy-link-dialog.component';
import { ViewService } from 'app/file-browser/services/view.service';

@Component({
  standalone: false,
  selector: 'app-workspace',
  templateUrl: './workspace.component.html',
  styleUrls: ['./workspace.component.scss'],
  encapsulation: ViewEncapsulation.None,
})
export class WorkspaceComponent implements OnInit {
  outlets$: Observable<string[]>;
  panes$: Observable<Pane[]>;

  constructor(
    protected readonly activatedRoute: ActivatedRoute,
    protected readonly workspaceManager: WorkspaceManager,
    protected readonly router: Router,
    protected readonly modalService: NgbModal,
    protected readonly viewService: ViewService,
  ) {}

  ngOnInit() {
    this.outlets$ = this.activatedRoute.data.pipe(
      switchMap(({ outlets$ }) => outlets$ as Observable<OutletsMap>),
      map(outlets => Object.keys(outlets ?? {})),
    );
    this.panes$ = this.workspaceManager.panes$;
    this.workspaceManager.initialLoad();
  }

  tabDropped(event: CdkDragDrop<Pane>) {
    const to = event.container.data;
    const from = event.previousContainer.data;
    this.workspaceManager.moveTab(from, event.previousIndex, to, event.currentIndex);
  }

  addTab(pane: Pane, url: string) {
    this.workspaceManager.openTabByUrl(pane, url);
  }

  duplicateTab(pane: Pane, tab: Tab) {
    this.workspaceManager.navigateByUrl({
      url: tab.url,
      extras: { newTab: true },
    });
  }

  copyLinkToTab(pane: Pane, tab: Tab) {
    const modalRef = this.modalService.open(CopyLinkDialogComponent);
    modalRef.componentInstance.url = 'Generating link...';
    const urlSubscription = this.viewService.getShareableLink(null, tab.url).subscribe(({ href }) => {
      modalRef.componentInstance.url = href;
    });
    modalRef.result.then(
      () => urlSubscription.unsubscribe(),
      () => urlSubscription.unsubscribe(),
    );
    return modalRef.result;
  }

  closeTab(pane: Pane, tab: Tab) {
    pane.deleteTab(tab);
    this.workspaceManager.save();
    this.workspaceManager.emitEvents();
  }

  closeOtherTabs(pane: Pane, tab: Tab) {
    this.closeTabs(pane, pane.tabs.filter(o => o !== tab));
  }

  closeAllTabs(pane: Pane) {
    this.closeTabs(pane, pane.tabs.slice());
  }

  closeTabs(pane: Pane, targetTabs: Tab[]) {
    for (const targetTab of targetTabs) {
      pane.deleteTab(targetTab);
    }
    this.workspaceManager.save();
    this.workspaceManager.emitEvents();
  }

  clearWorkbench() {
    for (const pane of this.workspaceManager.panes.panes) {
      this.closeAllTabs(pane);
    }
  }

  handleTabClick(e: MouseEvent, pane: Pane, tab: Tab) {
    if (e && (e.which === 2 || e.button === 4)) {
      this.closeTab(pane, tab);
    } else {
      this.setActiveTab(pane, tab);
    }
    e.preventDefault();
  }

  splitterDragEnded(result: { sizes: number[] }) {
    result.sizes.forEach((size, index) => {
      this.workspaceManager.panes.panes[index].size = size;
    });
    this.workspaceManager.save();
  }

  setActiveTab(pane: Pane, tab: Tab) {
    pane.activeTab = tab;
    this.workspaceManager.save();
    if (tab.url) {
      const segments = tab.url.replace(/^\//, '').split('/');
      this.router.navigate([{ outlets: { [pane.id]: segments } }]);
    }
  }

  setFocus(pane: Pane) {
    this.workspaceManager.focusedPane = pane;
  }

  canAddPane() {
    return this.workspaceManager.panes.panes.length === 1;
  }

  addPane() {
    this.workspaceManager.panes.getOrCreate('right');
    this.workspaceManager.save();
    this.workspaceManager.emitEvents();
  }

  closeRightPane() {
    this.workspaceManager.panes.delete(this.workspaceManager.panes.get('right'));
    this.workspaceManager.save();
    this.workspaceManager.emitEvents();
  }

  shouldConfirmUnload(): boolean {
    const result = this.workspaceManager.shouldConfirmUnload();
    if (result) {
      result.pane.activeTab = result.tab;
      return true;
    }
    return false;
  }

  @HostListener('window:beforeunload', ['$event'])
  handleBeforeUnload(event: BeforeUnloadEvent) {
    if (this.shouldConfirmUnload()) {
      event.returnValue = 'Leave page? Changes you made may not be saved';
    }
  }

  calculateFontAwesomeIcon(s: string) {
    if (s == null) {
      return 'window-maximize';
    } else if (s.includes(' ')) {
      return s;
    } else {
      return 'fa fa-' + s;
    }
  }
}
