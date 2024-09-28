import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';
import { CrudService } from '../../../servicios/crud.service';
import { EliminarPageRoutingModule } from './eliminar-routing.module';

import { EliminarPage } from './eliminar.page';
import { HttpClientModule } from '@angular/common/http';

@NgModule({
  imports: [
    CommonModule,
    IonicModule,
    EliminarPageRoutingModule,
    HttpClientModule
  ],
  declarations: [EliminarPage],
  providers:[CrudService]
})
export class EliminarPageModule {}
