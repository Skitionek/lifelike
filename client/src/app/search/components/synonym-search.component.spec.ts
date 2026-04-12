import { ComponentFixture, TestBed, waitForAsync } from '@angular/core/testing';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';

import { RootStoreModule } from 'app/root-store';
import { SharedModule } from 'app/shared/shared.module';

import { SynonymSearchComponent } from './synonym-search.component';
import { ContentSearchService } from '../services/content-search.service';

describe('SynonymSearchComponent', () => {
  let component: SynonymSearchComponent;
  let fixture: ComponentFixture<SynonymSearchComponent>;

  beforeEach(waitForAsync(() => {
    TestBed.configureTestingModule({
      imports: [
        RootStoreModule,
        SharedModule,
        BrowserAnimationsModule,
      ],
      declarations: [ SynonymSearchComponent ],
      providers: [
        ContentSearchService,
        NgbActiveModal,
      ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SynonymSearchComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
