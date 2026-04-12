import { ComponentFixture, TestBed, waitForAsync } from '@angular/core/testing';


import { LoadingIndicatorComponent } from './loading-indicator.component';

describe('LoadingIndicatorComponent', () => {
    let component: LoadingIndicatorComponent;
    let fixture: ComponentFixture<LoadingIndicatorComponent>;

    beforeEach(waitForAsync(() => {
        TestBed.configureTestingModule({
            declarations: [LoadingIndicatorComponent],
        })
    .compileComponents();
    }));

    beforeEach(() => {
        fixture = TestBed.createComponent(LoadingIndicatorComponent);
        component = fixture.componentInstance;
        fixture.detectChanges();
    });

    it('should create', () => {
        expect(component).toBeTruthy();
    });

    it('snapshot: should render the ellipsis container', () => {
        const el: HTMLElement = fixture.nativeElement;
        expect(el.querySelector('.lds-ellipsis')).not.toBeNull();
    });

    it('snapshot: should render four animated dots', () => {
        const el: HTMLElement = fixture.nativeElement;
        const dots = el.querySelectorAll('.lds-ellipsis div');
        expect(dots.length).toBe(4);
    });

    it('snapshot: rendered HTML should contain lds-ellipsis markup', () => {
        const html: string = fixture.nativeElement.innerHTML;
        expect(html).toContain('lds-ellipsis');
    });
});
