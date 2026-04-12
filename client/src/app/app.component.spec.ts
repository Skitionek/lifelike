import { ComponentFixture, TestBed, waitForAsync } from '@angular/core/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';


import { AppComponent } from 'app/app.component';
import { RootStoreModule } from 'app/root-store';
import { SharedModule } from 'app/shared/shared.module';

describe('AppComponent', () => {
  let fixture: ComponentFixture<AppComponent>;
  let instance: AppComponent;

  beforeEach(waitForAsync(() => {
    TestBed.configureTestingModule({
      imports: [
        RouterTestingModule,
        RootStoreModule,
        SharedModule,
        BrowserAnimationsModule,
      ],
      declarations: [
        AppComponent
      ],
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AppComponent);
    instance = fixture.debugElement.componentInstance;
  });

  it('should create the app', () => {
    expect(fixture).toBeTruthy();
  });
});
