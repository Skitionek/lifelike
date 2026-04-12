import { ComponentFixture, TestBed, waitForAsync } from '@angular/core/testing';

import { Subject } from 'rxjs';

import { GenericFileUploadComponent } from './generic-file-upload.component';

describe('GenericFileUploadComponent', () => {
    let component: GenericFileUploadComponent;
    let fixture: ComponentFixture<GenericFileUploadComponent>;

    beforeEach(waitForAsync(() => {
        TestBed.configureTestingModule({
            declarations: [ GenericFileUploadComponent ]
        })
    .compileComponents();
    }));

    beforeEach(() => {
        fixture = TestBed.createComponent(GenericFileUploadComponent);
        component = fixture.componentInstance;

        component.accept = 'xlsx';
        component.resetFileInputSubject = new Subject<boolean>();

        fixture.detectChanges();
    });

    it('should create', () => {
        expect(component).toBeTruthy();
    });
});
