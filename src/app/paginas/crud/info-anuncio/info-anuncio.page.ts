import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute} from '@angular/router';
import { CrudService } from "../../../servicios/crud.service"
import { obtenerDatosUsuario } from 'src/app/utilidades/usuario';

@Component({
  selector: 'app-info-anuncio',
  templateUrl: './info-anuncio.page.html',
  styleUrls: ['./info-anuncio.page.scss'],
})
export class InfoAnuncioPage implements OnInit {

  constructor(


  ) { }

  ngOnInit() {
  }

  anadirCarrito() {
  }

  ionViewDidEnter(){
    obtenerDatosUsuario();
  }
}
