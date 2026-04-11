import { Component, Input } from '@angular/core';

@Component({
  standalone: false,
  selector: 'app-sort-legend',
  templateUrl: './sort-legend.component.html',
})
export class SortLegendComponent {
  @Input() order: number | undefined;
  @Input() type: 'alpha' | 'numeric' | 'amount' = 'amount';
}
