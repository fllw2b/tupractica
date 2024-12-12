import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../services/api.service';
import { Router } from '@angular/router';
import { MenuController } from '@ionic/angular';

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

  // listas dinámicas para regiones, comunas y carreras
  regiones: any[] = [];
  comunas: any[] = [];
  carreras: any[] = [];

  maxFechaNacimiento: string = '';

  constructor(private apiService: ApiService,
    private router: Router,
    private menuCtrl: MenuController) {}

  ngOnInit() {
    this.setMaxFechaNacimiento();
    this.loadRegiones();
    this.loadCarreras();
  }

  setMaxFechaNacimiento() {
    const hoy = new Date();
    const hace18Anios = new Date(hoy.getFullYear() - 18, hoy.getMonth(), hoy.getDate());
    this.maxFechaNacimiento = hace18Anios.toISOString().split('T')[0];
  }

  // cargamos las regiones de la api
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

  ionViewWillEnter() {
    this.menuCtrl.enable(false);
  }

  ionViewWillLeave() {
    this.menuCtrl.enable(true);
  }

  // cargamos las carreras de la api
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

  // cargamos las comunas de la api
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
    formData.append('fecha_nacimiento', fechaFormateada);
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
