import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { Router, ActivatedRoute } from '@angular/router';
import { CrudService } from "./../../../servicios/crud.service"

import { obtenerDatosUsuario } from 'src/app/utilidades/usuario';
import { UsuarioConID } from "../../../modelos/usuario"

@Component({
  selector: 'app-modificar',
  templateUrl: './modificar.page.html',
  styleUrls: ['./modificar.page.scss'],
})
export class ModificarPage implements OnInit {

  public UsuarioLogeado: UsuarioConID;

  public idActiva = 0;
  

  public formulario: FormGroup;

  constructor(
    private fb: FormBuilder,
    private crudServicio: CrudService,
    private router: Router,
    private rutaActiva: ActivatedRoute,
    // cosas de filtrar usuario
  ) {
    this.formulario = this.fb.group({
    })
  }

  // MANEJO DE ERRORES
  public campo(control: string) {
    return this.formulario.get(control);
  }
  public errores(control: string) {
    return this.campo(control).errors
  }
  public esTocado(control: string) {
    return this.campo(control).touched;
  }
  public estaSucio(control: string) {
    return this.campo(control).dirty;
  }


  ngOnInit() {

  }


  ionViewDidEnter() {
    obtenerDatosUsuario();
  }
  

}
