import { ComponentFixture, TestBed, waitForAsync } from '@angular/core/testing';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { MockComponents } from 'ng-mocks';

import { LegendComponent } from './legend.component';
import { CollapsibleWindowComponent } from './collapsible-window.component';

describe('LegendComponent', () => {
    let component: LegendComponent;
    let fixture: ComponentFixture<LegendComponent>;

    beforeEach(waitForAsync(() => {
        TestBed.configureTestingModule({
            declarations: [
              LegendComponent,
              MockComponents(
                CollapsibleWindowComponent
              )
            ],
            imports: [
                BrowserAnimationsModule
            ]
        })
    .compileComponents();
    }));

    beforeEach(() => {
        fixture = TestBed.createComponent(LegendComponent);
        component = fixture.componentInstance;
        fixture.detectChanges();
    });

    it('should create', () => {
        expect(component).toBeTruthy();
    });
});
