import { Component, OnInit} from '@angular/core';
import { Router } from '@angular/router';
import { ProductoConID } from "../../../modelos/producto"
import { CrudService } from "../../../servicios/crud.service"

// cosas de filtrar usuario
import { UsuarioService } from "../../../servicios/usuario.service"
import { UsuarioConID } from "../../../modelos/usuario"


@Component({
  selector: 'app-listar',
  templateUrl: './listar.page.html',
  styleUrls: ['./listar.page.scss'],
})
export class ListarPage implements OnInit {
  // cosas de filtrar usuario
    public UsuarioLogeado:UsuarioConID;
    public esAdmin:boolean=false;

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
      this.obtenerDatosUsuario();
    }
    public obtenerDatosUsuario(){
      const usuario= localStorage.getItem('nombreusuario')
      if(!usuario){
        this.router.navigate(['']);
        }
        else
        {
          this.apiUsuario.buscarPorID(+usuario)
          .subscribe(usuarioactivo => {
            if(usuarioactivo){
              this.UsuarioLogeado = usuarioactivo;
              //this.esAdmin=this.UsuarioLogeado.isAdmin;
            }else{
              localStorage.removeItem('nombreusuario');
              this.router.navigate(['']);
            }
          })
      }
    }
    public soyadmin(){
      if(this.esAdmin){
        return true;
      }
      else{
        return null;
      }
    }
    public cerrarSession(){
      const usuario= localStorage.getItem('nombreusuario')
      if(!usuario){
        this.router.navigate(['']);
        }
        else
        {
            localStorage.removeItem('nombreusuario');
            this.router.navigate(['']);
        }
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

