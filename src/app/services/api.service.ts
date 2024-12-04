import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class ApiService {
  private baseUrl = 'http://127.0.0.1:8000/api'; // Base URL de tu API

  constructor(private http: HttpClient) {}

  // Iniciar sesión
  login(email: string, password: string): Observable<any> {
    return this.http.post(`${this.baseUrl}/login/`, { email, password });
  }


  // Registro de estudiantes
  register(data: any): Observable<any> {
    return this.http.post(`${this.baseUrl}/registro/estudiante/`, data);
  }

  // Obtener prácticas
  getPracticas(token: string): Observable<any> {
    const headers = new HttpHeaders({
      Authorization: `Bearer ${token}`,
    });
    return this.http.get(`${this.baseUrl}/practicas/`, { headers });
  }

  getAnuncioById(anuncioId: number): Observable<any> {
    return this.http.get(`${this.baseUrl}/practicas/${anuncioId}/`);
  }


  // Ver detalles de una práctica
  getDetallePractica(id: number, token: string): Observable<any> {
    const headers = new HttpHeaders({
      Authorization: `Bearer ${token}`,
    });
    return this.http.get(`${this.baseUrl}/practica/${id}/`, { headers });
  }

  // Postular a una práctica
  postularPractica(anuncioId: number, token: string): Observable<any> {
    const headers = new HttpHeaders({
      Authorization: `Bearer ${token}`,
    });
    return this.http.post(`${this.baseUrl}/postulacion/`, { anuncio_id: anuncioId }, { headers });
  }

  // Obtener historial de postulaciones
  getPostulaciones(): Observable<any> {

    const token = localStorage.getItem('access_token');
    const headers = new HttpHeaders({
      Authorization: `Bearer ${token}`,
    });
    return this.http.get(`${this.baseUrl}/postulaciones/`, { headers });
  }

  // Eliminar una postulación
  deletePostulacion(postulacionId: number): Observable<any> {
    const token = localStorage.getItem('access_token'); // Obtener el token automáticamente
    const headers = new HttpHeaders({
      Authorization: `Bearer ${token}`,
    });

    return this.http.delete(`${this.baseUrl}/postulacion/${postulacionId}/`, { headers });
  }


  getRegiones(): Observable<any> {
    return this.http.get(`${this.baseUrl}/regiones/`);
  }

  getComunas(regionId: number): Observable<any> {
    return this.http.get(`${this.baseUrl}/get-comunas/${regionId}/`);
  }

  getCarreras(): Observable<any> {
    return this.http.get(`${this.baseUrl}/carreras/`);
  }

  getPerfil(): Observable<any> {
    const token = localStorage.getItem('access_token');
    const headers = new HttpHeaders({
      Authorization: `Bearer ${token}`,
    });
    return this.http.get(`${this.baseUrl}/estudiante/detail/`, { headers });
  }

  getAnuncios(): Observable<any> {
    return this.http.get(`${this.baseUrl}/practicas/`);
  }
}


