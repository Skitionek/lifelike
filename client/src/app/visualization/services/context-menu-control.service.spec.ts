import { TestBed, waitForAsync } from '@angular/core/testing';


import { ContextMenuControlService } from './context-menu-control.service';

describe('ContextMenuControlService', () => {
    let service: ContextMenuControlService;

    beforeEach(waitForAsync(() => {
        TestBed.configureTestingModule(
            {providers: [ContextMenuControlService]},
        )
    .compileComponents();
    }));

    beforeEach(() => {
        // TODO: consider Angular 9?
        // see Note in docs about Testbed.get() not being type safe
        // https://angular.io/guide/testing#angular-testbed
        // Testbed.inject() is Angular 9: https://github.com/angular/angular/issues/34401
        service = TestBed.inject(ContextMenuControlService);
    });

    it('should be created', () => {
        expect(service).toBeTruthy();
    });
});
