import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { RegistroPageRoutingModule } from './registro-routing.module';

import { UsuarioService } from "../../../servicios/usuario.service"
import { RegistroPage } from './registro.page';
import { HttpClientModule } from '@angular/common/http';
@NgModule({
  imports: [
    CommonModule,
    ReactiveFormsModule,
    IonicModule,
    RegistroPageRoutingModule,
    HttpClientModule
  ],
  declarations: [RegistroPage],
  providers: [
    UsuarioService
  ]
})
export class RegistroPageModule {}
