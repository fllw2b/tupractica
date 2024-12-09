import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DetallePracticaPage } from './detalle-practica.page'; // Asegúrate de que esto sea correcto

const routes: Routes = [
  {
    path: '',
    component: DetallePracticaPage, // Este debe coincidir con el nombre exportado
  },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class DetallePracticaPageRoutingModule {}
