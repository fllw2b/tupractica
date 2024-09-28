import { Component, OnInit} from '@angular/core';
import { Router } from '@angular/router';
import { CrudService } from "../../../servicios/crud.service"


import { obtenerDatosUsuario,cerrarSession } from 'src/app/utilidades/usuario';


@Component({
  selector: 'app-listar',
  templateUrl: './listar.page.html',
  styleUrls: ['./listar.page.scss'],
})
export class ListarPage implements OnInit {
    constructor(
      private apiProducto: CrudService,
      private router: Router
    ) { }

    ngOnInit() {
    }

    ionViewDidEnter(){
      obtenerDatosUsuario();
    }
    

    public cerrarSession(){
        cerrarSession()
      }


    ionViewWillEnter(){
    }


    loadData(event) {
    }
  }

