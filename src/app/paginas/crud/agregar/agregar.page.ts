import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule} from '@angular/forms';
import { obtenerDatosUsuario } from 'src/app/utilidades/usuario';

@Component({
  selector: 'app-agregar',
  templateUrl: './agregar.page.html',
  styleUrls: ['./agregar.page.scss'],
})
export class AgregarPage implements OnInit {
  public formulario: FormGroup;

  constructor(
    private fb: FormBuilder,
  ) {
    this.formulario = this.fb.group(
    {   
    }
  )
}

  public campo(control: string){
    return this.formulario.get(control);
  }
  public errores(control: string){
    return this.campo(control).errors
  }
  public esTocado(control: string){
    return this.campo(control).touched;
  }
  public estaSucio(control: string){
    return this.campo(control).dirty;
  }

  ngOnInit() {
  }

  ionViewDidEnter() {
    obtenerDatosUsuario();
  }
}
