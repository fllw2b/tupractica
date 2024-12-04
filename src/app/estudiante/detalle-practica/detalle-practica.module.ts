import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { DetallePracticaPageRoutingModule } from './detalle-practica-routing.module';

import { AnuncioDetallePage } from './detalle-practica.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    DetallePracticaPageRoutingModule
  ],
  declarations: [AnuncioDetallePage]
})
export class DetallePracticaPageModule {}
