import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../services/api.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-practicas',
  templateUrl: './practicas.page.html',
  styleUrls: ['./practicas.page.scss'],
})
export class PracticasPage implements OnInit {
  anuncios: any[] = [];
  anunciosFiltrados: any[] = [];
  textoFiltro: string = '';
  modalidadFiltro: string = '';
  regionFiltro: string = '';
  regiones: any[] = [];

  constructor(
    private apiService: ApiService,
    private router: Router
  ) {}

  ngOnInit() {
    this.cargarRegiones();
    this.cargarAnuncios();
  }

  cargarRegiones() {
    this.apiService.getRegiones().subscribe(
      (res) => {
        this.regiones = res; // asignamos las regiones
      },
      (err) => {
        console.error('Error al cargar las regiones:', err);
      }
    );
  }

  cargarAnuncios() {
    this.apiService.getAnuncios().subscribe(
      (res) => {
        console.log('Anuncios cargados:', res); // vemos en la consola pa ver q funcione
        this.anuncios = res;
        this.anunciosFiltrados = [...this.anuncios];
      },
      (err) => {
        console.error('Error al cargar los anuncios:', err);
      }
    );
  }


  aplicarFiltros() {
    this.anunciosFiltrados = this.anuncios.filter((anuncio) => {
      const coincideTexto =
        this.textoFiltro === '' ||
        anuncio.titulo.toLowerCase().includes(this.textoFiltro.toLowerCase()) ||
        anuncio.descripcion.toLowerCase().includes(this.textoFiltro.toLowerCase());
      const coincideModalidad =
        this.modalidadFiltro === '' || anuncio.modalidad === this.modalidadFiltro;
      const coincideRegion =
        this.regionFiltro === '' || anuncio.region === this.regionFiltro;

      return coincideTexto && coincideModalidad && coincideRegion;
    });
  }

  verDetalleAnuncio(id: number) {
    this.router.navigate([`/detalle-practica/${id}`]);
  }
}
