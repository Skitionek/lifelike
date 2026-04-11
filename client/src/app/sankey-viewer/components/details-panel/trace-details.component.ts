import { Component } from '@angular/core';

import { SankeyDetailsComponent } from './details.component';

@Component({
  standalone: false,
  selector: 'app-sankey-trace-details',
  templateUrl: './trace-details.component.html'
})
export class SankeyTraceDetailsComponent extends SankeyDetailsComponent {
}
