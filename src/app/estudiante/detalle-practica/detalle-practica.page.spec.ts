import { ComponentFixture, TestBed } from '@angular/core/testing';
import { DetallePracticaPage } from './detalle-practica.page';

describe('DetallePracticaPage', () => {
  let component: DetallePracticaPage;
  let fixture: ComponentFixture<DetallePracticaPage>;

  beforeEach(() => {
    fixture = TestBed.createComponent(DetallePracticaPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
