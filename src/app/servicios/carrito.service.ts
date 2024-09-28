import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Carrito } from "./../modelos/carrito"
import { Producto } from "./../modelos/producto"
import { Observable,BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CarritoService {
  private URL_API = 'http://localhost:3000/carrito'
  public paginaActual = 1;
  constructor(
    private http: HttpClient,
    private cliente: HttpClient
  ) { }

  public crearCarrito(carrito: Carrito): Observable<any> {
    return this.http.post(this.URL_API, carrito, {
      headers: {
        'Content-Type': 'application/json; charset=utf-8'
      }
    })
  }

  public buscarPorID(id: number): Observable<Carrito | null> {
    return this.cliente.get<Carrito | null>(`${this.URL_API}/${id}`);
  }

  public modificarPorID(id:number, carrito:Carrito): Observable<any> {
    return this.cliente.patch(`${this.URL_API}/${id}`, carrito, {
      headers: {
        'Content-Type': 'application/json; charset=utf-8'
      }
    })
  }

}
