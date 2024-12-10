import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DetallePracticaPage } from './detalle-practica.page';

const routes: Routes = [
  {
    path: '',
    component: DetallePracticaPage,
  },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class DetallePracticaPageRoutingModule {}
