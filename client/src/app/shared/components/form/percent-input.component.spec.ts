import { ComponentFixture, TestBed, waitForAsync } from '@angular/core/testing';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';


import { PercentInputComponent } from './percent-input.component';

describe('PercentInputComponent', () => {
    let component: PercentInputComponent;
    let fixture: ComponentFixture<PercentInputComponent>;

    beforeEach(waitForAsync(() => {
        TestBed.configureTestingModule({
            declarations: [PercentInputComponent],
            imports: [CommonModule, FormsModule],
        })
    .compileComponents();
    }));

    beforeEach(() => {
        fixture = TestBed.createComponent(PercentInputComponent);
        component = fixture.componentInstance;
        component.inputId = 'test-percent';
        fixture.detectChanges();
    });

    it('should create', () => {
        expect(component).toBeTruthy();
    });

    it('should emit valueChange when the input changes', () => {
        let emittedValue: number | undefined;
        component.valueChange.subscribe((v) => (emittedValue = v));

        component.changed({ target: { value: '50' } });

        expect(emittedValue).toBeCloseTo(0.5);
    });

    it('should convert 100% input to 1.0', () => {
        let emittedValue: number | undefined;
        component.valueChange.subscribe((v) => (emittedValue = v));

        component.changed({ target: { value: '100' } });

        expect(emittedValue).toBeCloseTo(1.0);
    });

    it('should convert 0% input to 0.0', () => {
        component.value = 0.5;
        let emittedValue: number | undefined;
        component.valueChange.subscribe((v) => (emittedValue = v));

        component.changed({ target: { value: '0' } });

        expect(emittedValue).toBeCloseTo(0.0);
    });

    it('should not emit when value has not changed', () => {
        component.value = 0.5;
        let emitCount = 0;
        component.valueChange.subscribe(() => emitCount++);

        component.changed({ target: { value: '50' } });

        expect(emitCount).toBe(0);
    });

    it('should render an input of type number', () => {
        const el: HTMLElement = fixture.nativeElement;
        const input = el.querySelector('input[type="number"]');
        expect(input).not.toBeNull();
    });
});
