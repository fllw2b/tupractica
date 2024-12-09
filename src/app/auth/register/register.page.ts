import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../services/api.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-register',
  templateUrl: './register.page.html',
  styleUrls: ['./register.page.scss'],
})
export class RegisterPage implements OnInit {
  email: string = '';
  password: string = '';
  nombres: string = '';
  apellidos: string = '';
  rut: string = '';
  region_id: number | null = null;
  comuna_id: number | null = null;
  carrera_id: number | null = null;
  fecha_nacimiento: string = '';
  genero: string = '';
  direccion: string = '';
  telefono: string = '';
  foto: File | null = null;
  cv: File | null = null;

  // Listas dinámicas para regiones, comunas y carreras
  regiones: any[] = [];
  comunas: any[] = [];
  carreras: any[] = [];

  maxFechaNacimiento: string = '';

  constructor(private apiService: ApiService, private router: Router) {}

  ngOnInit() {
    this.setMaxFechaNacimiento();
    this.loadRegiones();
    this.loadCarreras();
  }

  setMaxFechaNacimiento() {
    const hoy = new Date();
    const hace18Anios = new Date(hoy.getFullYear() - 18, hoy.getMonth(), hoy.getDate());
    this.maxFechaNacimiento = hace18Anios.toISOString().split('T')[0]; // Formato YYYY-MM-DD
  }

  // Cargar regiones desde la API
  loadRegiones() {
    this.apiService.getRegiones().subscribe(
      (res) => {
        this.regiones = res;
      },
      (err) => {
        console.error('Error al cargar regiones:', err);
      }
    );
  }

  // Cargar carreras desde la API
  loadCarreras() {
    this.apiService.getCarreras().subscribe(
      (res) => {
        this.carreras = res;
      },
      (err) => {
        console.error('Error al cargar carreras:', err);
      }
    );
  }

  // Cargar comunas cuando se selecciona una región
  onRegionChange() {
    if (this.region_id) {
      this.apiService.getComunas(this.region_id).subscribe(
        (res) => {
          this.comunas = res;
        },
        (err) => {
          console.error('Error al cargar comunas:', err);
        }
      );
    }
  }

  // Manejar los cambios de archivos para la foto y el CV
  onFileChange(event: any, type: string) {
    const file = event.target.files[0];
    if (type === 'foto') {
      this.foto = file;
    } else if (type === 'cv') {
      this.cv = file;
    }
  }

  register() {
    const formData = new FormData();
    const fechaFormateada = new Date(this.fecha_nacimiento).toISOString().split('T')[0];
    formData.append('fecha_nacimiento', fechaFormateada);
    formData.append('email', this.email);
    formData.append('password', this.password);
    formData.append('nombres', this.nombres);
    formData.append('apellidos', this.apellidos);
    formData.append('rut', this.rut);
    formData.append('region_id', this.region_id?.toString() || '');
    formData.append('comuna_id', this.comuna_id?.toString() || '');
    formData.append('carrera_id', this.carrera_id?.toString() || '');
    formData.append('fecha_nacimiento', fechaFormateada); // Usar fecha formateada
    formData.append('genero', this.genero);
    formData.append('direccion', this.direccion);
    formData.append('telefono', this.telefono);

    if (this.foto) {
      formData.append('foto', this.foto);
    }
    if (this.cv) {
      formData.append('cv', this.cv);
    }

    this.apiService.register(formData).subscribe(
      (res) => {
        console.log('Registro exitoso:', res);
        alert('Registro exitoso. Ahora puedes iniciar sesión.');
        this.router.navigate(['/login']);
      },
      (err) => {
        console.error('Error al registrarse:', err);
        alert('Error al registrarse. Verifica los datos ingresados.');
      }
    );
  }

  // Redirigir al login
  navigateToLogin() {
    this.router.navigate(['/login']);
  }

  uploadFile(type: string): void {
    const input = document.createElement('input');
    input.type = 'file';
    input.accept = type === 'foto' ? 'image/*' : '.pdf,.doc,.docx';
    input.onchange = (event: any) => {
      const file = event.target.files[0];
      if (type === 'foto') {
        this.foto = file;
      } else if (type === 'cv') {
        this.cv = file;
      }
      console.log(`${type} seleccionado:`, file);
    };
    input.click();
  }

}
