import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute} from '@angular/router';
import { ProductoConID } from "../../../modelos/producto";
import { CrudService } from "../../../servicios/crud.service"
import { productoConCantidad } from 'src/app/modelos/carrito';
import { obtenerDatosUsuario } from 'src/app/utilidades/usuario';

import { CarritoService } from "../../../servicios/carrito.service"
// cosas de filtrar usuario
import { UsuarioService } from "../../../servicios/usuario.service"
import { UsuarioConID } from "../../../modelos/usuario"

@Component({
  selector: 'app-info-producto',
  templateUrl: './info-producto.page.html',
  styleUrls: ['./info-producto.page.scss'],
})
export class InfoProductoPage implements OnInit {
  public idActiva = '';
  public productoActivo!: ProductoConID;
  public productoCarrito: productoConCantidad;
  // cosas de filtrar usuario
  constructor(

  // cosas de filtrar usuario
    private apiUsuario: UsuarioService,
    private rutaActiva: ActivatedRoute,
    private router: Router,
    private apiProducto: CrudService,
    private apiCarrito: CarritoService,
  ) { }

  ngOnInit() {
    this.rutaActiva.params.subscribe(parametros => {
      this.idActiva = parametros.id;
      this.apiProducto.buscarPorID(+this.idActiva)
      .subscribe(producto => {
        if(producto){
          this.productoActivo = producto;
        }else {
          this.router.navigate(['../listar']);
        }
      })
    });
  }

  anadirCarrito() {
    this.apiProducto.buscarPorID(+this.idActiva)
      .subscribe(producto => {
        if (producto) {
          this.productoActivo = producto;
          this.productoCarrito = {
            'cantidad': 1,
            'producto': this.productoActivo
          }
          this.apiCarrito.buscarPorID(+localStorage.getItem('usuario'))
            .subscribe(carro => {
              if(carro.productos.length>0){
                for (var i = 0; i < carro.productos.length; i++) {
                  if(carro.productos[i].producto.id==producto.id){
                    carro.productos[i].cantidad=carro.productos[i].cantidad+1
                    this.apiCarrito.modificarPorID(+localStorage.getItem('usuario'), carro)
                    .subscribe()

                    this.router.navigate(['carrito']);
                    break
                  }else{if(i==carro.productos.length-1){
                    carro.productos = carro.productos.concat(this.productoCarrito)

                    this.apiCarrito.modificarPorID(+localStorage.getItem('usuario'), carro)
                    .subscribe()
                    this.router.navigate(['carrito']);
                    break
                  }
                }
              }
              }else{
                carro.productos = carro.productos.concat(this.productoCarrito)

                this.apiCarrito.modificarPorID(+localStorage.getItem('usuario'), carro)
                .subscribe()
                this.router.navigate(['carrito']);
              }
            }
          )
        }
      })
      ;
  }

// cosas de filtrar usuario
  ionViewDidEnter(){
    obtenerDatosUsuario();
  }


}
