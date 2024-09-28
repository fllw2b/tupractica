import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-login',
  templateUrl: './login.page.html',
  styleUrls: ['./login.page.scss'],
})
export class LoginPage implements OnInit {
  public login: FormGroup;
  constructor(
    private fb: FormBuilder,
    private http: HttpClient,
    private router: Router
  ) {
    this.login = this.fb.group({
      nombreusuario:[''],
      contrasena: ['',
        Validators.required
      ],
    });
  }

  logearse() {
    const nombreUsuario = this.login.value.nombreusuario;
    const contrasena = this.login.value.contrasena;
  
    // Construir la URL con el nombre de usuario y la contraseña
    const url = `http://localhost:8000/USUARIOC/${nombreUsuario}/${contrasena}/`;
  
    this.http.get<any>(url)
      .subscribe(
        res => {
          // Verifica si el usuario existe y si la contraseña es correcta
          if (res && res.contrasena === true) {
            // Aquí puedes procesar el usuario
            this.login.reset();
            localStorage.setItem('nombreusuario', res.nombreusuario); // Ajusta según la estructura de la respuesta
            this.router.navigate(["listar"]);
          } else {
            alert("Usuario y/o contraseña incorrectos.");
          }
        },
        err => {
          console.error("Error al conectar con la API:", err);
          alert("Nuestros servicios no se encuentran disponibles.");
        }
      );
  }
  



  ngOnInit() {
    const usuario= localStorage.getItem('nombreusuario')
      if(usuario){
      localStorage.removeItem('nombreusuario');
      }
  }




  }
