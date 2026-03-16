import { ComponentFixture, TestBed } from '@angular/core/testing';

import { configureTestSuite } from 'ng-bullet';
import { MockComponents } from 'ng-mocks';

import { LoadingIndicatorComponent } from './loading-indicator.component';
import { ModuleProgressComponent } from './module-progress.component';

describe('ModuleProgressComponent', () => {
    let component: ModuleProgressComponent;
    let fixture: ComponentFixture<ModuleProgressComponent>;

    configureTestSuite(() => {
        TestBed.configureTestingModule({
            declarations: [
                ModuleProgressComponent,
                MockComponents(LoadingIndicatorComponent),
            ],
        });
    });

    beforeEach(() => {
        fixture = TestBed.createComponent(ModuleProgressComponent);
        component = fixture.componentInstance;
        fixture.detectChanges();
    });

    it('should create', () => {
        expect(component).toBeTruthy();
    });

    it('snapshot: should apply default host class binding', () => {
        const el: HTMLElement = fixture.nativeElement;
        expect(el.className).toContain('position-absolute');
        expect(el.className).toContain('w-100');
        expect(el.className).toContain('h-100');
    });

    it('snapshot: should render loading-indicator inside the progress wrapper', () => {
        const el: HTMLElement = fixture.nativeElement;
        expect(el.querySelector('app-loading-indicator')).not.toBeNull();
    });

    it('snapshot: rendered HTML should contain the flex layout wrapper', () => {
        const html: string = fixture.nativeElement.innerHTML;
        expect(html).toContain('d-flex');
        expect(html).toContain('flex-column');
    });
});
