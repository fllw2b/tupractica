import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class PracticasService {
  private baseUrl = 'https://deploytry-production.up.railway.app/api';

  constructor(private http: HttpClient) {}

  getPracticas(): Observable<any> {
    return this.http.get(`${this.baseUrl}/practicas/`);
  }

  getDetallePractica(id: number): Observable<any> {
    return this.http.get(`${this.baseUrl}/practica/${id}/`);
  }

  postularPractica(anuncioId: number): Observable<any> {
    return this.http.post(`${this.baseUrl}/postulacion/`, { anuncio_id: anuncioId });
  }

  getHistorialPostulaciones(): Observable<any> {
    return this.http.get(`${this.baseUrl}/postulaciones/`);
  }

  deletePostulacion(id: number): Observable<any> {
    return this.http.delete(`${this.baseUrl}/postulacion/${id}/`);
  }
}
