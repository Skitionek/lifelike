import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { NgChartsModule } from 'ng2-charts';

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
    NgChartsModule
  ],
  exports: components,
})
export class ChartModule {

}
