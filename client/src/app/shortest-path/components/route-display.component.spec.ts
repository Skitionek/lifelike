import { ComponentFixture, TestBed, waitForAsync } from '@angular/core/testing';

import { MockComponents } from 'ng-mocks';

import { PlotlySankeyDiagramComponent } from 'app/shared/components/plotly-sankey-diagram/plotly-sankey-diagram.component';
import { VisJsNetworkComponent } from 'app/shared/components/vis-js-network/vis-js-network.component';

import { RouteDisplayComponent } from './route-display.component';

describe('RouteDisplayComponent', () => {
  let component: RouteDisplayComponent;
  let fixture: ComponentFixture<RouteDisplayComponent>;

  beforeEach(waitForAsync(() => {
    TestBed.configureTestingModule({
      declarations: [
        RouteDisplayComponent,
        MockComponents(
          PlotlySankeyDiagramComponent,
          VisJsNetworkComponent
        )
      ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(RouteDisplayComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
