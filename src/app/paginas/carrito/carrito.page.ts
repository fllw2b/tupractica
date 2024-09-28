import { Component, OnInit } from '@angular/core';
import { ProductoConID } from 'src/app/modelos/producto';
import { Router, ActivatedRoute} from '@angular/router';

import { productoConCantidad,Carrito } from 'src/app/modelos/carrito';
import { CarritoService } from "../../servicios/carrito.service"

// cosas de filtrar usuario
import { UsuarioService } from "./../../servicios/usuario.service"
import { UsuarioConID } from "./../../modelos/usuario"

import { obtenerDatosUsuario } from 'src/app/utilidades/usuario';

@Component({
  selector: 'app-carrito',
  templateUrl: './carrito.page.html',
  styleUrls: ['./carrito.page.scss'],
})
export class CarritoPage implements OnInit {
  // cosas de filtrar usuario
    public UsuarioLogeado:UsuarioConID;
    public idActiva = 0;
    public carrito:Carrito;
    public total:number=0;
    public productosenelcarro:Array<productoConCantidad>;
    public cooldown: boolean = false;
    constructor(
      private apiUsuario: UsuarioService,
      private router: Router,
      private apiCarrito: CarritoService,
    ) { }

    ngOnInit() {
      this.total=0;
        this.idActiva = +localStorage.getItem('usuario');
        this.apiCarrito.buscarPorID(+this.idActiva)
        .subscribe(carritox => {
          if(carritox){
            this.carrito = carritox;
            this.productosenelcarro=this.carrito.productos;
            for (var i = 0; i < this.carrito.productos.length; i++) {
              this.total=this.total+(this.carrito.productos[i].cantidad*this.carrito.productos[i].producto.precio)
            }
          }else {
            alert("ha ocurrido un error inesperado")
            this.router.navigate(['']);
          }
        })
      ;
    }
    public vaciarCarrito(){
            this.carrito.productos=[]
            this.apiCarrito.modificarPorID(+localStorage.getItem('usuario'),this.carrito)
            .subscribe()
            this.total=0;
            setTimeout(() => {
              this.ngOnInit();
            }, 500);
          }

    public productoMas(i:number,x:number){
      this.cooldown = true;
      this.carrito.productos[i].cantidad=this.carrito.productos[i].cantidad+x;
      if(this.carrito.productos[i].cantidad <= 0){
        this.carrito.productos.splice( i, 1 );
      }
      this.apiCarrito.modificarPorID(+localStorage.getItem('usuario'),this.carrito)
        .subscribe()
        setTimeout(() => {
          this.cooldown = false;
          this.ngOnInit();
        }, 500);
    }

    // cosas de filtrar usuario
      ionViewDidEnter(){
        obtenerDatosUsuario();
      }
}



