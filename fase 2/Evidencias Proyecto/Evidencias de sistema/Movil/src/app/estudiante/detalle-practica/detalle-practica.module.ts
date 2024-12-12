import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { IonicModule } from '@ionic/angular';
import { DetallePracticaPageRoutingModule } from './detalle-practica-routing.module';
import { DetallePracticaPage } from './detalle-practica.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    DetallePracticaPageRoutingModule,
  ],
  declarations: [DetallePracticaPage],
})
export class DetallePracticaPageModule {}
