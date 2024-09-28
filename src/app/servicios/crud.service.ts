import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';
import { Producto, ProductoConID, ProductoParcial} from "./../modelos/producto"

@Injectable({
  providedIn: 'root'
})
export class CrudService {
  private URL_API = 'http://localhost:3000/productos';
  public paginaActual = 1;
  private comProducto = new BehaviorSubject<Array<ProductoConID>>([]);
  public listaProductos$ = this.comProducto.asObservable();
  constructor(
    private cliente: HttpClient
  ) { }
  public agregarNuevo(producto: Producto): Observable<any> {
    return this.cliente.post(this.URL_API, producto, {
      headers: {
        'Content-Type': 'application/json; charset=utf-8'
      }
    })
  }
  public obtenerPrimeros10Productos(){
    this.cliente.get<Array<ProductoConID>>(`${this.URL_API}?_page=1`)
    .subscribe(datos => {
      this.paginaActual = 1;
      this.paginaActual = this.paginaActual + 1;
      this.comProducto.next(datos);
    })
  }
  public obtener10Mas(){
    this.cliente.get<Array<ProductoConID>>(`${this.URL_API}?_page=${this.paginaActual}`)
    .subscribe(datos => {
      this.paginaActual = this.paginaActual + 1;
      const arrayActual = this.comProducto.getValue()
      this.comProducto.next(arrayActual.concat(datos));
    })
  }
  public buscarPorID(id: number): Observable<ProductoConID | null> {
    return this.cliente.get<ProductoConID | null>(`${this.URL_API}/${id}`);
  }
  public eliminarPorID(id: number): Observable<any> {
    return this.cliente.delete(`${this.URL_API}/${id}`);
  }
  public modificarPorID(id:number, producto: ProductoParcial): Observable<any> {
    return this.cliente.patch(`${this.URL_API}/${id}`, producto, {
      headers: {
        'Content-Type': 'application/json; charset=utf-8'
      }
    })
  }

}
