import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, FormControl, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { UsuarioService } from "../../../servicios/usuario.service";


@Component({
  selector: 'app-registro',
  templateUrl: './registro.page.html',
  styleUrls: ['./registro.page.scss'],
})
export class RegistroPage implements OnInit {

  public formulario: FormGroup;

  constructor(
    private fb: FormBuilder,
    private usuarioServicio: UsuarioService,

    private router: Router,
    private http: HttpClient
  ) {
    this.formulario = this.fb.group({
      nombreusuario: ['', [
        Validators.required,
        Validators.minLength(3),
        Validators.maxLength(15)
      ]],
      email: ['', [
        Validators.required,
        Validators.minLength(3),
        Validators.maxLength(20),
        Validators.email
      ]],
      contrasena: ['', [
        Validators.required,
        Validators.minLength(4),
        Validators.maxLength(20)
      ]],
    });
  }

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
  public guardarUsuario() {
    if (this.formulario.invalid) {
      this.formulario.markAllAsTouched();
      return;
    }
    this.http.get<any>("http://127.0.0.1:8000/USUARIO/")
    .subscribe(res => {
      const usuario = res.find((a: any) => {
        return a.usuario === this.formulario.value.nombreusuario
      });
      if (usuario) {
        alert('Nombre de usuario no disponible.');
        this.router.navigate(['registro']);
      } else {
        this.usuarioServicio.agregarNuevo(this.formulario.value,
        )
          .subscribe(dato => {
            if (dato) {
//              this.carrito.usuario=dato;
//              this.carritoServicio.crearCarrito(this.carrito).subscribe()
              alert("Usuario registrado correctamente.");
              this.formulario.reset();
              this.formulario.updateValueAndValidity();
              this.router.navigate(['']);
            }
          }, err => {
            // Verifica el código de estado y muestra el alert correspondiente
            if (err.status === 422) {
                alert("Formato de Email Incorrecto");
            } else {
                alert("Error: " + JSON.stringify(err));
                // Puedes manejar otros errores aquí si es necesario
            }
        });
    }
}, err => {  
    alert("Error al obtener usuarios: " + JSON.stringify(err)); 
    //alert("Nuestros servicios no se encuentran disponibles.")
});
}

  ngOnInit() {
  }

}

