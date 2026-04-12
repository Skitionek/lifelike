import { ComponentFixture, TestBed, waitForAsync } from '@angular/core/testing';

import { MockComponents } from 'ng-mocks';

import { LegendComponent } from '../legend.component';
import { PlotlySankeyDiagramComponent } from './plotly-sankey-diagram.component';

describe('PlotlySankeyDiagramComponent', () => {
  let component: PlotlySankeyDiagramComponent;
  let fixture: ComponentFixture<PlotlySankeyDiagramComponent>;

  beforeEach(waitForAsync(() => {
    TestBed.configureTestingModule({
      declarations: [
        PlotlySankeyDiagramComponent,
        MockComponents(
          LegendComponent
        ),
      ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    (window as any).Plotly = { newPlot: jasmine.createSpy('newPlot').and.returnValue(Promise.resolve()) };

    fixture = TestBed.createComponent(PlotlySankeyDiagramComponent);
    component = fixture.componentInstance;

    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
