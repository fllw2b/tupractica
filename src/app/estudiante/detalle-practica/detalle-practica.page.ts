import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ApiService } from '../../services/api.service';

@Component({
  selector: 'app-detalle-practica',
  templateUrl: './detalle-practica.page.html',
  styleUrls: ['./detalle-practica.page.scss'],
})
export class AnuncioDetallePage implements OnInit {
  anuncio: any = null;

  constructor(private route: ActivatedRoute, private apiService: ApiService) {}

  ngOnInit() {
    const anuncioId = this.route.snapshot.paramMap.get('id');
    this.loadAnuncio(anuncioId);
  }

  loadAnuncio(anuncioId: string | null) {
    if (anuncioId) {
      this.apiService.getAnuncioById(parseInt(anuncioId, 10)).subscribe(
        (res) => {
          this.anuncio = res;
        },
        (err) => {
          console.error('Error al cargar el anuncio:', err);
        }
      );
    }
  }
}
