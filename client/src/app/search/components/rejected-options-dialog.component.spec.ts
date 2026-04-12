import { ComponentFixture, TestBed, waitForAsync } from '@angular/core/testing';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';

import { RootStoreModule } from 'app/root-store';
import { SharedModule } from 'app/shared/shared.module';

import { RejectedOptionsDialogComponent } from './rejected-options-dialog.component';
import { ContentSearchService } from '../services/content-search.service';

describe('RejectedOptionsDialogComponent', () => {
  let component: RejectedOptionsDialogComponent;
  let fixture: ComponentFixture<RejectedOptionsDialogComponent>;

  beforeEach(waitForAsync(() => {
    TestBed.configureTestingModule({
      imports: [
        RootStoreModule,
        SharedModule,
        BrowserAnimationsModule,
      ],
      declarations: [ RejectedOptionsDialogComponent ],
      providers: [
        ContentSearchService,
        NgbActiveModal,
      ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(RejectedOptionsDialogComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
