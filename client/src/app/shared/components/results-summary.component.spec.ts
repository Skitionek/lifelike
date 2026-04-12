import { ComponentFixture, TestBed } from '@angular/core/testing';
import { CommonModule } from '@angular/common';

import { configureTestSuite } from 'ng-bullet';

import { ResultsSummaryComponent } from './results-summary.component';

describe('ResultsSummaryComponent', () => {
    let component: ResultsSummaryComponent;
    let fixture: ComponentFixture<ResultsSummaryComponent>;

    configureTestSuite(() => {
        TestBed.configureTestingModule({
            declarations: [ResultsSummaryComponent],
            imports: [CommonModule],
        });
    });

    beforeEach(() => {
        fixture = TestBed.createComponent(ResultsSummaryComponent);
        component = fixture.componentInstance;
        component.page = 1;
        component.pageSize = 10;
        component.collectionSize = 50;
        fixture.detectChanges();
    });

    it('should create', () => {
        expect(component).toBeTruthy();
    });

    it('should compute startResultCount for the first page', () => {
        component.page = 1;
        component.pageSize = 10;
        expect(component.startResultCount).toBe(1);
    });

    it('should compute startResultCount for subsequent pages', () => {
        component.page = 3;
        component.pageSize = 10;
        expect(component.startResultCount).toBe(21);
    });

    it('should compute endResultCount within a full page', () => {
        component.page = 1;
        component.pageSize = 10;
        component.collectionSize = 50;
        expect(component.endResultCount).toBe(10);
    });

    it('should compute endResultCount on the last partial page', () => {
        component.page = 6;
        component.pageSize = 10;
        component.collectionSize = 55;
        expect(component.endResultCount).toBe(55);
    });

    it('should render "results" in the template for multiple items', () => {
        fixture.detectChanges();
        const html: string = fixture.nativeElement.textContent;
        expect(html).toContain('results');
    });

    it('should render "result" (singular) in the template when collectionSize is 1', () => {
        component.page = 1;
        component.pageSize = 10;
        component.collectionSize = 1;
        fixture.detectChanges();
        const html: string = fixture.nativeElement.textContent;
        expect(html).toContain('result');
        expect(html).not.toContain('results');
    });
});
