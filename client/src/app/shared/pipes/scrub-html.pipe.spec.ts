import { inject, TestBed, waitForAsync } from '@angular/core/testing';
import { BrowserModule, DomSanitizer } from '@angular/platform-browser';


import { ScrubHtmlPipe } from './scrub-html.pipe';

describe('ScrubHtmlPipe', () => {
  beforeEach(waitForAsync(() => {
    TestBed.configureTestingModule({
      imports: [
        BrowserModule
      ]
    })
    .compileComponents();
  }));

  it('create an instance', inject([DomSanitizer], (domSanitizer: DomSanitizer) => {
    const pipe = new ScrubHtmlPipe(domSanitizer);
    expect(pipe).toBeTruthy();
  }));
});
