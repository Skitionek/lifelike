import { Component, Input, OnChanges, SimpleChanges } from '@angular/core';
import { ChartData, ChartOptions, ChartType } from 'chart.js';

import { EnrichWithGOTermsResult } from 'app/enrichment/services/enrichment-visualisation.service';

@Component({
  standalone: false,
  selector: 'app-chart',
  templateUrl: './chart.component.html',
  styleUrls: ['./chart.component.scss'],
})
export class ChartComponent implements OnChanges {
  public options: ChartOptions = {
    responsive: true,
    maintainAspectRatio: false,
    indexAxis: 'y',
    scales: {
      x: {
        min: 0,
        ticks: {
          stepSize: 1,
        },
        grid: {
          drawOnChartArea: false
        },
        type: 'logarithmic' as const,
        title: {
          display: true,
          text: '-log(q-value)'
        }
      }
    } as any,
    plugins: {
      datalabels: {
        display: false
      },
      tooltip: {
        enabled: true,
        mode: 'y',
        intersect: false,
        callbacks: {
          title: ([tooltipItem]) => {
            const dataIndex = tooltipItem.dataIndex;
            return (this.chartData?.datasets?.[0]?.data?.[dataIndex] as any)?.gene ?? '';
          },
          label: (tooltipItem) => {
            const dataIndex = tooltipItem.dataIndex;
            const d = this.chartData?.datasets?.[0]?.data?.[dataIndex] as any;
            return d ? `q-value: ${d['q-value'].toExponential(2)}` : '';
          }
        }
      },
      legend: {
        display: false
      }
    } as any
  };
  public chartType: ChartType = 'bar';
  legend = false;

  @Input() showMore: boolean;
  @Input() data: EnrichWithGOTermsResult[];
  @Input() show: boolean;

  chartData: ChartData;
  labels: string[];

  ngOnChanges({show, data, showMore}: SimpleChanges) {
    if (this.show && (show || data || showMore)) {
      const slicedNotFormatedData = this.showMore ? this.data.slice(0, 50) : this.data.slice(0, 10);
      const xValues = slicedNotFormatedData.map((d: any) => ({
        ...d,
        x: -Math.log(d['q-value'])
      }));
      this.labels = slicedNotFormatedData.map(({gene}) => gene);
      this.chartData = {
        labels: this.labels,
        datasets: [{
          data: xValues.map(d => d.x),
          backgroundColor: 'gray'
        }]
      };
    }
  }
}
