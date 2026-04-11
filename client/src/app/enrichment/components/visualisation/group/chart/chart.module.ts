import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { BaseChartDirective } from 'ng2-charts';

import { SharedModule } from 'app/shared/shared.module';

import { ChartComponent } from './chart.component';

const components = [
  ChartComponent
];

@NgModule({
  declarations: components,
  imports: [
    CommonModule,
    SharedModule,
    BaseChartDirective
  ],
  exports: components,
})
export class ChartModule {

}
