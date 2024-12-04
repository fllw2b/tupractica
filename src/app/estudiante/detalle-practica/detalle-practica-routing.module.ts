import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AnuncioDetallePage } from './detalle-practica.page';

const routes: Routes = [
  {
    path: '',
    component: AnuncioDetallePage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class DetallePracticaPageRoutingModule {}
