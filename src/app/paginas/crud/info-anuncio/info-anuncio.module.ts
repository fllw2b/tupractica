import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { InfoAnuncioPageRoutingModule } from './info-anuncio-routing.module';

import { InfoAnuncioPage } from './info-anuncio.page';
import { HttpClientModule } from '@angular/common/http';
import { CrudService } from '../../../servicios/crud.service';

@NgModule({
  imports: [
    CommonModule,
    IonicModule,
    InfoAnuncioPageRoutingModule,
    HttpClientModule
  ],
  declarations: [InfoAnuncioPage],
  providers: [CrudService]
})
export class InfoAnuncioPageModule {}
