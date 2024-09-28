import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { ProductoConID } from "../../../modelos/producto";
import { CrudService } from "../../../servicios/crud.service"
// cosas de filtrar usuario
import { UsuarioService } from "../../../servicios/usuario.service"
import { UsuarioConID } from "../../../modelos/usuario"

import { obtenerDatosUsuario } from 'src/app/utilidades/usuario';
@Component({
  selector: 'app-eliminar',
  templateUrl: './eliminar.page.html',
  styleUrls: ['./eliminar.page.scss'],
})
export class EliminarPage implements OnInit {

  // cosas de filtrar usuario
  public UsuarioLogeado: UsuarioConID;
  public idActiva = '';
  public productoActivo!: ProductoConID;
  constructor(
    // cosas de filtrar usuario
    private apiUsuario: UsuarioService,
    private rutaActiva: ActivatedRoute,
    private router: Router,
    private apiProducto: CrudService
  ) { }
  ngOnInit() {
    this.rutaActiva.params.subscribe(parametros => {
      this.idActiva = parametros.id;
      this.apiProducto.buscarPorID(+this.idActiva)
        .subscribe(producto => {
          if (producto) {
            this.productoActivo = producto;
          } else {
            this.router.navigate(['/listar']);
          }
        })
    });
  }
  public borrar() {
    this.apiProducto.eliminarPorID(+this.idActiva)
      .subscribe(dato => {
        if (dato) {
          alert('Producto eliminado con éxito.');
          this.router.navigate(['/listar']);
        }
      })
  }
   ionViewDidEnter() {
    obtenerDatosUsuario();
  }
}
