import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ApiService } from '../../services/api.service';

@Component({
  selector: 'app-practicas',
  templateUrl: './practicas.page.html',
  styleUrls: ['./practicas.page.scss'],
})
export class PracticasPage implements OnInit {
  anuncios: any[] = [];

  constructor(private apiService: ApiService, private router: Router) {}

  ngOnInit() {
    this.loadAnuncios();
  }

  loadAnuncios() {
    this.apiService.getAnuncios().subscribe(
      (res) => {
        this.anuncios = res;
      },
      (err) => {
        console.error('Error al cargar anuncios:', err);
      }
    );
  }

  verDetalleAnuncio(anuncioId: number) {
    this.router.navigate([`/detalle-practica`, anuncioId]);
  }
}
