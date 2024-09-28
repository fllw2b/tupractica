import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { IonicModule } from '@ionic/angular';
import { LoginPageRoutingModule } from './login-routing.module';
import { LoginPage } from './login.page';
import { UsuarioService } from 'src/app/servicios/usuario.service';
import { ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';

@NgModule({
  imports: [
    CommonModule,
    ReactiveFormsModule,
    IonicModule,
    HttpClientModule,
    LoginPageRoutingModule
  ],
  declarations: [LoginPage],
  providers: [
    UsuarioService
  ]
})
export class LoginPageModule {}
