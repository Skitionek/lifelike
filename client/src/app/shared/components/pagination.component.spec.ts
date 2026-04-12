import { ComponentFixture, TestBed, waitForAsync } from '@angular/core/testing';
import { CommonModule } from '@angular/common';

import { NgbModule } from '@ng-bootstrap/ng-bootstrap';

import { PaginationComponent } from './pagination.component';
import { PaginatedRequestOptions } from '../schemas/common';

describe('PaginationComponent', () => {
    let component: PaginationComponent;
    let fixture: ComponentFixture<PaginationComponent>;

    beforeEach(waitForAsync(() => {
        TestBed.configureTestingModule({
            declarations: [PaginationComponent],
            imports: [CommonModule, NgbModule],
        })
    .compileComponents();
    }));

    beforeEach(() => {
        fixture = TestBed.createComponent(PaginationComponent);
        component = fixture.componentInstance;
        fixture.detectChanges();
    });

    it('should create', () => {
        expect(component).toBeTruthy();
    });

    it('should have alwaysShow as false by default', () => {
        expect(component.alwaysShow).toBeFalse();
    });

    it('should have collectionSize as 0 by default', () => {
        expect(component.collectionSize).toBe(0);
    });

    it('should emit pageChange with updated page when goToPage is called', () => {
        const paging: PaginatedRequestOptions = { page: 1, limit: 10 };
        component.paging = paging;
        fixture.detectChanges();

        let emittedValue: PaginatedRequestOptions | undefined;
        component.pageChange.subscribe((value) => (emittedValue = value));

        component.goToPage(3);

        expect(emittedValue).toEqual({ page: 3, limit: 10 });
    });

    it('should preserve other paging properties when navigating to a page', () => {
        const paging: PaginatedRequestOptions = { page: 1, limit: 25, sort: 'name' };
        component.paging = paging;
        fixture.detectChanges();

        let emittedValue: PaginatedRequestOptions | undefined;
        component.pageChange.subscribe((value) => (emittedValue = value));

        component.goToPage(2);

        expect(emittedValue).toEqual({ page: 2, limit: 25, sort: 'name' });
    });

    it('should render placeholder pagination when paging is undefined', () => {
        component.paging = undefined;
        fixture.detectChanges();
        const el: HTMLElement = fixture.nativeElement;
        expect(el.querySelector('.pagination')).not.toBeNull();
    });
});
