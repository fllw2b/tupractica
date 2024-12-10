import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../services/api.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-editar-perfil',
  templateUrl: './editar-perfil.page.html',
  styleUrls: ['./editar-perfil.page.scss'],
})
export class EditarPerfilPage implements OnInit {
  perfil: any = {};
  regiones: any[] = [];
  comunas: any[] = [];
  carreras: any[] = [];

  constructor(private apiService: ApiService, private router: Router) {}

  ngOnInit() {
    this.cargarDatosIniciales();
  }

  cargarDatosIniciales() {
    // Carga las regiones, comunas y carreras
    this.apiService.getPerfil().subscribe((perfil) => {
      this.perfil = perfil;
      this.cargarRegiones();
      this.cargarCarreras();
      this.cargarComunas(perfil.region_id);
    });
  }

  cargarCarreras() {
    this.apiService.getCarreras().subscribe((res) => {
      this.carreras = res;
    });
  }


  guardarCambios() {
    const formData = new FormData();
    formData.append('nombres', this.perfil.nombres);
    formData.append('apellidos', this.perfil.apellidos);
    formData.append('telefono', this.perfil.telefono);
    formData.append('direccion', this.perfil.direccion);

    // incluye la región y comuna
    formData.append('region_id', this.perfil.region_id);
    formData.append('comuna_id', this.perfil.comuna_id);

    this.apiService.updatePerfil(formData).subscribe(
      () => {
        alert('Perfil actualizado con éxito');
        this.router.navigate(['/perfil']);
      },
      (err) => {
        console.error('Error al actualizar el perfil:', err);
        alert('Ocurrió un error al guardar los cambios.');
      }
    );
  }

  cargarRegiones() {
    this.apiService.getRegiones().subscribe(
      (res) => {
        this.regiones = res;
      },
      (err) => {
        console.error('Error al cargar las regiones:', err);
      }
    );
  }

  cargarComunas(regionId: string) {
    if (!regionId) return;

    const numericRegionId = parseInt(regionId, 10); // Convierte a número

    this.apiService.getComunas(numericRegionId).subscribe(
      (res) => {
        this.comunas = res;
      },
      (err) => {
        console.error('Error al cargar las comunas:', err);
      }
    );
  }


}

