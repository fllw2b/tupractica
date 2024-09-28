import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { CarritoPageRoutingModule } from './carrito-routing.module';
import { HttpClientModule } from '@angular/common/http';
import { CarritoService } from '../../servicios/carrito.service';
import { CarritoPage } from './carrito.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    CarritoPageRoutingModule
  ],
  declarations: [CarritoPage],
  providers: [CarritoService]
})
export class CarritoPageModule {}
