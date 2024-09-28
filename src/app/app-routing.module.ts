import { NgModule } from '@angular/core';
import { PreloadAllModules, RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  {
    path: 'listar',
    loadChildren: () => import('./paginas/crud/listar/listar.module').then( m => m.ListarPageModule)
  },
  {
    path: 'agregar',
    loadChildren: () => import('./paginas/crud/agregar/agregar.module').then( m => m.AgregarPageModule)
  },
  {
    path: 'eliminar/:id',
    loadChildren: () => import('./paginas/crud/eliminar/eliminar.module').then( m => m.EliminarPageModule)
  },
  {
    path: 'modificar/:id',
    loadChildren: () => import('./paginas/crud/modificar/modificar.module').then( m => m.ModificarPageModule)
  },
  {
    path: '',
    loadChildren: () => import('./paginas/usuario/login/login.module').then( m => m.LoginPageModule)
  },
  {
    path: 'registro',
    loadChildren: () => import('./paginas/usuario/registro/registro.module').then( m => m.RegistroPageModule)
  },
  {
    path: 'info-producto/:id',
    loadChildren: () => import('./paginas/crud/info-producto/info-producto.module').then( m => m.InfoProductoPageModule)
  },
  {
    path: 'carrito',
    loadChildren: () => import('./paginas/carrito/carrito.module').then( m => m.CarritoPageModule)
  },
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes, { preloadingStrategy: PreloadAllModules })
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }
