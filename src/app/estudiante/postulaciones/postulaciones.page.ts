import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../services/api.service';

@Component({
  selector: 'app-postulaciones',
  templateUrl: './postulaciones.page.html',
  styleUrls: ['./postulaciones.page.scss'],
})
export class PostulacionesPage implements OnInit {
  postulaciones: any[] = [];

  constructor(private apiService: ApiService) {}

  ngOnInit() {
    this.loadPostulaciones();
  }

  loadPostulaciones() {
    this.apiService.getPostulaciones().subscribe(
      (res) => {
        this.postulaciones = res;
        console.log('Postulaciones cargadas:', this.postulaciones);
      },
      (err) => {
        console.error('Error al cargar postulaciones:', err);
      }
    );
  }

  cancelarPostulacion(postulacionId: number) {
    this.apiService.deletePostulacion(postulacionId).subscribe(
      () => {
        this.postulaciones = this.postulaciones.filter(p => p.id !== postulacionId);
        alert('Postulación cancelada correctamente.');
      },
      (err) => {
        console.error('Error al cancelar postulación:', err);
        alert('Hubo un error al cancelar la postulación.');
      }
    );
  }

}
