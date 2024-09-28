import { Component, OnInit } from '@angular/core';
import { obtenerDatosUsuario } from 'src/app/utilidades/usuario';
@Component({
  selector: 'app-eliminar',
  templateUrl: './eliminar.page.html',
  styleUrls: ['./eliminar.page.scss'],
})
export class EliminarPage implements OnInit {

  
  constructor(

  ) { }
  ngOnInit() {
  }
   ionViewDidEnter() {
    obtenerDatosUsuario();
  }
}
