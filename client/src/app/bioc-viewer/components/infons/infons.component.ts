import { Component, Input } from '@angular/core';


@Component({
  standalone: false,
  selector: 'app-bioc-infons',
  templateUrl: './infons.component.html',
  styleUrls: ['./infons.component.scss'],
})
export class InfonsComponent {
  @Input() data;
}
