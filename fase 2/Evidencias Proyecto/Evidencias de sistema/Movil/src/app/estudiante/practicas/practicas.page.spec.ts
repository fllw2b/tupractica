import { ComponentFixture, TestBed } from '@angular/core/testing';
import { PracticasPage } from './practicas.page';

describe('PracticasPage', () => {
  let component: PracticasPage;
  let fixture: ComponentFixture<PracticasPage>;

  beforeEach(() => {
    fixture = TestBed.createComponent(PracticasPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
