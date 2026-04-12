import { ComponentFixture, TestBed, waitForAsync } from '@angular/core/testing';


import { SortLegendComponent } from './sort-legend.component';

describe('SortLegendComponent', () => {
    let component: SortLegendComponent;
    let fixture: ComponentFixture<SortLegendComponent>;

    beforeEach(waitForAsync(() => {
        TestBed.configureTestingModule({
            declarations: [SortLegendComponent],
        })
    .compileComponents();
    }));

    beforeEach(() => {
        fixture = TestBed.createComponent(SortLegendComponent);
        component = fixture.componentInstance;
        fixture.detectChanges();
    });

    it('should create', () => {
        expect(component).toBeTruthy();
    });

    it('should not render an icon when order is undefined', () => {
        component.order = undefined;
        fixture.detectChanges();
        const el: HTMLElement = fixture.nativeElement;
        expect(el.querySelector('i')).toBeNull();
    });

    it('should render an icon when order is set', () => {
        component.order = 1;
        fixture.detectChanges();
        const el: HTMLElement = fixture.nativeElement;
        expect(el.querySelector('i')).not.toBeNull();
    });

    it('should use "amount" as default type', () => {
        expect(component.type).toBe('amount');
    });

    it('should reflect the "alpha" type in the icon class', () => {
        component.order = 1;
        component.type = 'alpha';
        fixture.detectChanges();
        const el: HTMLElement = fixture.nativeElement;
        expect(el.querySelector('i').className).toContain('alpha');
    });

    it('should reflect the "numeric" type in the icon class', () => {
        component.order = 1;
        component.type = 'numeric';
        fixture.detectChanges();
        const el: HTMLElement = fixture.nativeElement;
        expect(el.querySelector('i').className).toContain('numeric');
    });
});
