import { ComponentFixture, TestBed, waitForAsync } from '@angular/core/testing';


import { RootStoreModule } from 'app/root-store';

import { DrawingToolModule } from '../../drawing-tool.module';
import { PaletteComponent } from './palette.component';

describe('PaletteComponent', () => {
    let component: PaletteComponent;
    let fixture: ComponentFixture<PaletteComponent>;

    beforeEach(waitForAsync(() => {
        TestBed.configureTestingModule({
            imports: [
              DrawingToolModule,
              RootStoreModule
            ]
        })
    .compileComponents();
    }));

    beforeEach(() => {
        fixture = TestBed.createComponent(PaletteComponent);
        component = fixture.componentInstance;
        fixture.detectChanges();
    });

    it('should create', () => {
        expect(component).toBeTruthy();
    });
});
