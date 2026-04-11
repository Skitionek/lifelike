import { Component, Input } from '@angular/core';

@Component({
  standalone: false,
  selector: 'app-results-summary',
  templateUrl: './results-summary.component.html',
})
export class ResultsSummaryComponent {
  @Input() page: number; // pages should be 1-indexed
  @Input() pageSize: number;
  @Input() collectionSize: number;
  @Input() resultCountLimited?: boolean;
  @Input() resultLimit?: number;

  get startResultCount(): number {
    return (this.pageSize * (this.page - 1)) + 1;
  }

  get endResultCount(): number {
    return Math.min(this.pageSize * this.page, this.collectionSize);
  }
}
