import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { ApiService } from '../../services/api.service';

@Component({
  selector: 'app-detalle-practica',
  templateUrl: './detalle-practica.page.html',
  styleUrls: ['./detalle-practica.page.scss'],
})
export class DetallePracticaPage implements OnInit {
  practica: any = null;
  postulado: boolean = false;

  constructor(
    private route: ActivatedRoute,
    private apiService: ApiService,
    private router: Router
  ) {}

  ngOnInit() {
    const practicaId = this.route.snapshot.paramMap.get('id');
    const token = localStorage.getItem('access_token');

    if (!token) {
      alert('Sesión expirada. Por favor, inicia sesión nuevamente.');
      this.router.navigate(['/login']);
      return;
    }

    if (practicaId) {
      this.loadPractica(parseInt(practicaId, 10));
      this.checkPostulacion(parseInt(practicaId, 10));
    }
  }

  loadPractica(practicaId: number) {
    this.apiService.getPracticaById(practicaId).subscribe(
      (res) => {
        this.practica = res;
      },
      (err) => {
        console.error('Error al cargar la práctica:', err);
      }
    );
  }

  checkPostulacion(practicaId: number) {
    this.apiService.verificarPostulacion(practicaId).subscribe(
      (res) => {
        this.postulado = res.postulado;
      },
      (err) => {
        console.error('Error al verificar la postulación:', err);
      }
    );
  }

  postular() {
    if (!this.practica) return;

    this.apiService.postularPractica(this.practica.id, localStorage.getItem('access_token') || '').subscribe(
      () => {
        this.postulado = true;
        alert('Postulación realizada con éxito.');
      },
      (error) => {
        console.error('Error al postular:', error);
        alert(error.error.message || 'Error al intentar postular.');
      }
    );
  }
}
