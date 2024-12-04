import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../services/api.service';

@Component({
  selector: 'app-perfil',
  templateUrl: './perfil.page.html',
  styleUrls: ['./perfil.page.scss'],
})
export class PerfilPage implements OnInit {
  perfil: any = null;

  constructor(private apiService: ApiService) {}

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
    // Lógica para editar el perfil (redirección o modal)
    console.log('Redirigiendo a editar perfil...');
  }
}
