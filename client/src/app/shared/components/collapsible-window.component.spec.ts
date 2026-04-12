import { ComponentFixture, TestBed } from '@angular/core/testing';
import { CommonModule } from '@angular/common';

import { configureTestSuite } from 'ng-bullet';

import { CollapsibleWindowComponent } from './collapsible-window.component';
import { SharedDirectivesModule } from '../directives/shareddirectives.module';

describe('CollapsibleWindowComponent', () => {
    let component: CollapsibleWindowComponent;
    let fixture: ComponentFixture<CollapsibleWindowComponent>;

    configureTestSuite(() => {
        TestBed.configureTestingModule({
            declarations: [CollapsibleWindowComponent],
            imports: [CommonModule, SharedDirectivesModule],
        });
    });

    beforeEach(() => {
        fixture = TestBed.createComponent(CollapsibleWindowComponent);
        component = fixture.componentInstance;
        fixture.detectChanges();
    });

    it('should create', () => {
        expect(component).toBeTruthy();
    });

    it('should be expanded by default', () => {
        expect(component.expanded).toBeTrue();
    });

    it('should collapse when collapse() is called', () => {
        component.collapse();
        expect(component.expanded).toBeFalse();
    });

    it('should expand when expand() is called', () => {
        component.collapse();
        component.expand();
        expect(component.expanded).toBeTrue();
    });

    it('should toggle from expanded to collapsed', () => {
        component.expanded = true;
        component.toggle();
        expect(component.expanded).toBeFalse();
    });

    it('should toggle from collapsed to expanded', () => {
        component.expanded = false;
        component.toggle();
        expect(component.expanded).toBeTrue();
    });

    it('should render the title in the template', () => {
        component.title = 'Test Window';
        fixture.detectChanges();
        const el: HTMLElement = fixture.nativeElement;
        expect(el.textContent).toContain('Test Window');
    });

    it('should show window content when expanded', () => {
        component.expanded = true;
        fixture.detectChanges();
        const el: HTMLElement = fixture.nativeElement;
        expect(el.querySelector('.overflow-auto')).not.toBeNull();
    });

    it('should hide window content when collapsed', () => {
        component.collapse();
        fixture.detectChanges();
        const el: HTMLElement = fixture.nativeElement;
        expect(el.querySelector('.overflow-auto')).toBeNull();
    });
});
