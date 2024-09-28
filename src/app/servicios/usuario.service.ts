import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Usuario,UsuarioConID,UsuarioParcial } from "./../modelos/usuario"
import { Observable,BehaviorSubject } from 'rxjs';
import { Encriptar } from '../utilidades/usuario';

@Injectable({
  providedIn: 'root'
})
export class UsuarioService {
  private URL_API = 'http://127.0.0.1:8000/USUARIO/'
  public paginaActual = 1;

  constructor(
    private cliente: HttpClient
  ) { }

  public agregarNuevo(usuario: Usuario): Observable<any> {
    usuario.contrasena=Encriptar(usuario.contrasena)
    return this.cliente.post(this.URL_API, usuario, {
      headers: {
        'Content-Type': 'application/json; charset=utf-8'
      }
    })
  }


  public buscarPorID(id: number): Observable<UsuarioConID | null> {
    return this.cliente.get<UsuarioConID | null>(`${this.URL_API}/${id}`);
  }

}
