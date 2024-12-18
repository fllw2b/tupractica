import { Component, OnInit, ChangeDetectorRef } from '@angular/core';
import { Router } from '@angular/router';
import { MenuController } from '@ionic/angular';
import { AuthService } from './services/auth.service';

@Component({
  selector: 'app-root',
  templateUrl: 'app.component.html',
  styleUrls: ['app.component.scss'],
})
export class AppComponent implements OnInit {
  isLoggedIn = false;

  menuOptions: { title: string; path: string; action?: () => void }[] = [];

  constructor(
    private router: Router,
    private menuCtrl: MenuController,
    private authService: AuthService,
    private cdRef: ChangeDetectorRef
  ) {}

  ngOnInit() {
    this.authService.isAuthenticated$.subscribe({
      next: (isAuthenticated: boolean) => {
        this.isLoggedIn = isAuthenticated;
        this.updateMenuOptions();
        this.cdRef.detectChanges();
      },
      error: (err) => console.error('Error al suscribirse al estado de autenticación:', err),
    });
    this.isLoggedIn = this.authService.getAuthState();
    this.updateMenuOptions();
  }

  updateMenuOptions() {
    if (this.isLoggedIn) {
      this.menuOptions = [
        { title: 'Mi Perfil', path: '/perfil' },
        { title: 'Mis Postulaciones', path: '/postulaciones' },
        { title: 'Anuncios', path: '/practicas' },
        {
          title: 'Cerrar Sesión',
          path: '/login',
          action: () => this.logout(),
        },
      ];
    } else {
      this.menuOptions = [
        { title: 'Iniciar Sesión', path: '/login' },
        { title: 'Registrarse', path: '/registro' },
      ];
    }
  }

  navigateTo(path: string) {
    this.router.navigate([path]).then(() => {
      this.menuCtrl.close();
    });
  }

  logout() {
    this.authService.logout();
    this.isLoggedIn = false;
    this.updateMenuOptions();
    this.router.navigate(['/login']).then(() => {
      this.menuCtrl.close();
    });
  }
}
