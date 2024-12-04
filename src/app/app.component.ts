import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { MenuController } from '@ionic/angular';
@Component({
  selector: 'app-root',
  templateUrl: 'app.component.html',
  styleUrls: ['app.component.scss'],
})
export class AppComponent {
  constructor(private router: Router, private menuCtrl: MenuController) {}

  navigateTo(path: string) {
    this.router.navigate([path]).then(() => {
      this.menuCtrl.close(); // Cerrar el menú después de redirigir
    });
  }

  logout() {
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    this.router.navigate(['/login']).then(() => {
      this.menuCtrl.close(); // Cerrar el menú después de cerrar sesión
    });
}
}
