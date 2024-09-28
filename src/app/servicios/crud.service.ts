import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CrudService {
  private URL_API = 'http://localhost:3000/PENDIENTE';
  public paginaActual = 1;
  constructor(
    private cliente: HttpClient
  ) { }

}
