import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../services/api.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-perfil',
  templateUrl: './perfil.page.html',
  styleUrls: ['./perfil.page.scss'],
})
export class PerfilPage implements OnInit {
  perfil: any = null;

  constructor(private apiService: ApiService, private router: Router) {}

  ngOnInit() {
    this.loadPerfil();
  }

  loadPerfil() {
    this.apiService.getPerfil().subscribe(
      (res) => {
        this.perfil = res;
      },
      (err) => {
        console.error('Error al cargar perfil:', err);
      }
    );
  }

  editarPerfil() {
    this.router.navigate(['/editar-perfil']);
  }

  verCV(cvUrl: string) {
    if (cvUrl) {
      window.open(cvUrl, '_blank'); // Abre el CV en una nueva pestaña
    } else {
      alert('No se ha subido un CV.');
    }
  }

  cargarDatosIniciales() {
    this.apiService.getPerfil().subscribe(
      (perfil) => {
        console.log('Datos del perfil:', perfil); // Muestra los datos en consola
        this.perfil = perfil;
      },
      (err) => {
        console.error('Error al cargar el perfil:', err);
        alert('Ocurrió un error al obtener los datos del perfil.');
      }
    );
  }

}

