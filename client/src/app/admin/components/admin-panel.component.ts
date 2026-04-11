import { Component } from '@angular/core';

/**
 * The administration panel.
 */
@Component({
  standalone: false,
  selector: 'app-admin-panel',
  templateUrl: 'admin-panel.component.html',
})
export class AdminPanelComponent {
  /**
   * The currently active tab.
   */
  activeTab: 'users';

  constructor() {
  }
}
