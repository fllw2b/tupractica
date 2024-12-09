import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../services/api.service';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-postulaciones',
  templateUrl: './postulaciones.page.html',
  styleUrls: ['./postulaciones.page.scss'],
})
export class PostulacionesPage implements OnInit {
  postulaciones: any[] = [];

  constructor(
    private route: ActivatedRoute,
    private apiService: ApiService,
    private router: Router
  ) {}

  ngOnInit() {
    this.loadPostulaciones();
  }

  loadPostulaciones() {
    this.apiService.getPostulaciones().subscribe(
      (res) => {
        console.log('Postulaciones cargadas:', res);
        this.postulaciones = res;
      },
      (err) => {
        console.error('Error al cargar postulaciones:', err);
        if (err.status === 401) {
          alert('Tu sesión ha expirado. Por favor, inicia sesión nuevamente.');
          this.router.navigate(['/login']); // Redirige al login si el token no es válido
        }
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
