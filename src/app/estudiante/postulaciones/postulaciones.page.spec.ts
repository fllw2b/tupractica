import { ComponentFixture, TestBed } from '@angular/core/testing';
import { PostulacionesPage } from './postulaciones.page';

describe('PostulacionesPage', () => {
  let component: PostulacionesPage;
  let fixture: ComponentFixture<PostulacionesPage>;

  beforeEach(() => {
    fixture = TestBed.createComponent(PostulacionesPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
