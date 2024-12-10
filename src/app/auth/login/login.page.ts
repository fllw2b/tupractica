import { Component } from '@angular/core';
import { ApiService } from '../../services/api.service';
import { Router } from '@angular/router';
import { MenuController } from '@ionic/angular';

@Component({
  selector: 'app-login',
  templateUrl: './login.page.html',
  styleUrls: ['./login.page.scss'],
})
export class LoginPage {
  email: string = '';
  password: string = '';

  constructor(private apiService: ApiService,
    private router: Router,
    private menuCtrl: MenuController) {}

  ionViewWillEnter() {
    this.menuCtrl.enable(false);
  }

  ionViewWillLeave() {
    this.menuCtrl.enable(true);
  }

  login() {
    if (!this.email || !this.password) {
      console.error('Por favor, completa todos los campos.');
      return;
    }

    this.apiService.login(this.email, this.password).subscribe(
      (res) => {
        localStorage.setItem('access_token', res.access);
        localStorage.setItem('refresh_token', res.refresh);
        this.router.navigate(['/practicas']);
      },
      (err) => {
        console.error('Error al iniciar sesión:', err);
        alert('Error al iniciar sesión. Verifica tus credenciales.');
      }
    );
  }
  navigateToRegister() {
    this.router.navigate(['/register']);
  }
}
