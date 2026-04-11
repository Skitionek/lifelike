import { Component, OnInit, OnDestroy } from '@angular/core';
import { MatSnackBar } from '@angular/material/snack-bar';
import { HttpClient } from '@angular/common/http';

import { Subscription } from 'rxjs';
import { ChartData, ChartDataset, ChartOptions } from 'chart.js';

import { BackgroundTask } from 'app/shared/rxjs/background-task';

interface StatisticsDataResponse {
  [domain: string]: {
    [entity: string]: number
  };
}

const ENTITY_COLORS = [
  'rgba(30, 130, 76, 0.9)',
  'rgba(235, 149, 50, 0.9)',
  'rgba(226, 106, 106, 0.9)',
  'rgba(31, 58, 147, 0.9)',
  'rgba(242, 120, 75, 0.9)',
  'rgba(153, 0, 102, 0.9)',
  'rgba(144, 198, 149, 0.9)',
  'rgba(27, 163, 156, 0.9)',
  'rgba(153, 102, 0, 0.9)',
  'rgba(44, 130, 201, 0.9)',
  'rgba(150, 40, 27, 0.9)',
  'rgba(153, 204, 204, 0.9)',
  'rgba(78, 205, 196, 0.9)',
  'rgba(137, 196, 244, 0.9)',
  'rgba(51, 110, 123, 0.9)',
  'rgba(58, 83, 155, 0.9)',
  'rgba(51, 0, 102, 0.9)',
];

const DOMAIN_COLORS = [
  'rgba(34, 167, 240, 0.9)',
  'rgba(169, 109, 173, 0.9)',
  'rgba(38, 194, 129, 0.9)',
  'rgba(245, 230, 83, 0.9)',
  'rgba(242, 121, 53, 0.9)',
  'rgba(149, 165, 166, 0.9)',
  'rgba(129, 207, 224, 0.9)',
  'rgba(250, 190, 88, 0.9)',
  'rgba(0, 181, 204, 0.9)',
];

@Component({
  standalone: false,
  selector: 'app-kg-statistics',
  templateUrl: './kg-statistics.component.html',
  styleUrls: ['./kg-statistics.component.scss']
})
export class KgStatisticsComponent {
  loadTask: BackgroundTask<void, StatisticsDataResponse>;

  allDomainsChartData: ChartData<'bar'>;
  entitiesByDomainChartData: { [domain: string]: ChartData<'bar'> } = {};

  chartOptions: ChartOptions<'bar'> = {
    responsive: true,
    maintainAspectRatio: false,
    indexAxis: 'y',
    scales: {
      y: {
        ticks: {
          callback: (value) => this.addThousandSeparator(value.toString())
        },
      },
      x: {
        beginAtZero: true,
        ticks: {
          callback: (value) => this.addThousandSeparator(value.toString())
        }
      }
    },
    plugins: {
      datalabels: {
        formatter: (value) => this.addThousandSeparator(value.toString()),
        anchor: 'end',
        offset: 0,
        align: 'end',
        font: {
          size: 14
        }
      },
      legend: { display: false },
      tooltip: {
        callbacks: {
          label: (tooltipItem) => this.addThousandSeparator(tooltipItem.formattedValue)
        }
      }
    } as any,
    layout: {
      padding: {
        top: 25,
        right: 50
      }
    },
  };

  barChartOptions: ChartOptions<'bar'> = {
    ...this.chartOptions,
    indexAxis: 'x',
  };

  totalCount: any = 0;

  constructor(private http: HttpClient, private snackBar: MatSnackBar) {
    this.loadTask = new BackgroundTask<void, StatisticsDataResponse>(() => {
      return this.http.get<StatisticsDataResponse>('/api/kg-statistics');
    });

    this.loadTask.results$.subscribe(({result, value}) => {
      this._getChartDataEntitiesByDomain(result);
      this._getChartDataAllDomains(result);
    });

    this.refresh();
  }

  refresh() {
    this.loadTask.update();
  }

  private _getChartDataEntitiesByDomain(statisticsData: StatisticsDataResponse) {
    const entityToColor: { [entity: string]: string } = {};
    let i = 0;
    for (const domainData of Object.values(statisticsData)) {
      Object.keys(domainData).forEach(entity => {
        if (!entityToColor.hasOwnProperty(entity)) {
          entityToColor[entity] = ENTITY_COLORS[i % ENTITY_COLORS.length];
          i += 1;
        }
      });
    }

    this.entitiesByDomainChartData = {};
    for (const [domain, domainData] of Object.entries(statisticsData)) {
      const labels: string[] = [];
      const data: number[] = [];
      const backgroundColor: string[] = [];
      for (const [entity, count] of Object.entries(domainData)) {
        labels.push(entity);
        data.push(count);
        backgroundColor.push(entityToColor[entity]);
      }
      this.entitiesByDomainChartData[domain] = {
        labels,
        datasets: [{ data, backgroundColor, maxBarThickness: 50 }]
      };
    }
  }

  private _getChartDataAllDomains(statisticsData: StatisticsDataResponse) {
    const labels: string[] = [];
    const data: number[] = [];
    for (const [domain, domainData] of Object.entries(statisticsData)) {
      labels.push(domain);
      data.push(Object.values(domainData).reduce((a, b) => a + b, 0));
    }
    this.allDomainsChartData = {
      labels,
      datasets: [{ data, backgroundColor: DOMAIN_COLORS }]
    };
    this.totalCount = data.reduce((a, b) => a + b, 0);
  }

  addThousandSeparator(value: string) {
    return value.replace(/\B(?=(\d{3})+(?!\d))/g, ',');
  }

}
