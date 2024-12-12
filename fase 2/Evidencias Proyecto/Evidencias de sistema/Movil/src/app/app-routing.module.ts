import { NgModule } from '@angular/core';
import { PreloadAllModules, RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  {
    path: '',
    redirectTo: 'login',
    pathMatch: 'full',
  },
  {
    path: 'login',
    loadChildren: () => import('./auth/login/login.module').then(m => m.LoginPageModule),
  },
  {
    path: 'register',
    loadChildren: () => import('./auth/register/register.module').then( m => m.RegisterPageModule)
  },
  {
    path: 'perfil',
    loadChildren: () => import('./estudiante/perfil/perfil.module').then( m => m.PerfilPageModule)
  },
  { path: 'practicas', loadChildren: () => import('./estudiante/practicas/practicas.module').then(m => m.PracticasPageModule) },
  {
    path: 'postulaciones',
    loadChildren: () => import('./estudiante/postulaciones/postulaciones.module').then( m => m.PostulacionesPageModule)
  },
  { path: 'detalle-practica/:id', loadChildren: () => import('./estudiante/detalle-practica/detalle-practica.module').then(m => m.DetallePracticaPageModule) },
  {
    path: 'editar-perfil',
    loadChildren: () => import('./estudiante/editar-perfil/editar-perfil.module').then( m => m.EditarPerfilPageModule)
  },
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes, { preloadingStrategy: PreloadAllModules })
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }
