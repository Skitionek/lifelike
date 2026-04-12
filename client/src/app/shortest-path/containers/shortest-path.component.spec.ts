import { ComponentFixture, TestBed, waitForAsync } from '@angular/core/testing';

import { MockComponents } from 'ng-mocks';

import { RootStoreModule } from 'app/root-store';
import { SharedModule } from 'app/shared/shared.module';

import { RouteBuilderComponent } from '../components/route-builder.component';
import { RouteDisplayComponent } from '../components/route-display.component';
import { ShortestPathComponent } from './shortest-path.component';

describe('ShortestPathComponent', () => {
  let component: ShortestPathComponent;
  let fixture: ComponentFixture<ShortestPathComponent>;

  beforeEach(waitForAsync(() => {
    TestBed.configureTestingModule({
      imports: [
        RootStoreModule,
        SharedModule,
      ],
      declarations: [
        ShortestPathComponent,
        MockComponents(
          RouteBuilderComponent,
          RouteDisplayComponent,
      ),
      ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ShortestPathComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
