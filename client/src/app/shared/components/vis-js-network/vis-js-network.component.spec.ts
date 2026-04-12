import { ComponentFixture, TestBed, waitForAsync } from '@angular/core/testing';
import { FormsModule } from '@angular/forms';

import { MockComponents } from 'ng-mocks';

import { CollapsibleWindowComponent } from '../collapsible-window.component';
import { LegendComponent } from '../legend.component';
import { SearchControlComponent } from '../search-control.component';
import { VisJsNetworkComponent } from './vis-js-network.component';

describe('VisJsNetworkComponent', () => {
  let component: VisJsNetworkComponent;
  let fixture: ComponentFixture<VisJsNetworkComponent>;

  beforeEach(waitForAsync(() => {
    TestBed.configureTestingModule({
      imports: [
        // This import is for the ngModel input of the app-search-control-component
        FormsModule
      ],
      declarations: [
        VisJsNetworkComponent,
        MockComponents(
          LegendComponent,
          SearchControlComponent,
          CollapsibleWindowComponent,
        ),
      ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(VisJsNetworkComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
