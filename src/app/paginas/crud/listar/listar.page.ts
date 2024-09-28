import { Component, OnInit} from '@angular/core';
import { Router } from '@angular/router';
import { ProductoConID } from "../../../modelos/producto"
import { CrudService } from "../../../servicios/crud.service"

// cosas de filtrar usuario
import { UsuarioService } from "../../../servicios/usuario.service"
import { UsuarioConID } from "../../../modelos/usuario"

import { obtenerDatosUsuario } from 'src/app/utilidades/usuario';


@Component({
  selector: 'app-listar',
  templateUrl: './listar.page.html',
  styleUrls: ['./listar.page.scss'],
})
export class ListarPage implements OnInit {
  // cosas de filtrar usuario
    public UsuarioLogeado:UsuarioConID;

    public productos: Array<ProductoConID> = [];
    constructor(
      private apiProducto: CrudService,
      // cosas de filtrar usuario
      private apiUsuario: UsuarioService,

      private router: Router
    ) { }

    ngOnInit() {
    }
    // cosas de filtrar usuario
    ionViewDidEnter(){
      obtenerDatosUsuario();
    }
    

    public cerrarSession(){
      const usuario= localStorage.getItem('nombreusuario')
      if(usuario){
        localStorage.removeItem('nombreusuario');
        }
      this.router.navigate(['']);
      }


    ionViewWillEnter(){
      this.apiProducto.obtenerPrimeros10Productos();
      this.apiProducto.listaProductos$.subscribe(datos => {
      this.productos = datos;
      });
    }
    handleRefresh(event) {
      setTimeout(() => {
        this.ionViewWillEnter();
        event.target.complete();
      }, 2000);
    };

    loadData(event) {
      setTimeout(() => {
        this.apiProducto.obtener10Mas();
        this.apiProducto.listaProductos$.subscribe(datos => {
        this.productos = datos;
        });
        event.target.complete()
      }, 500);
    }
  }

