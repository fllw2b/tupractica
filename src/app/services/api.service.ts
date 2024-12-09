import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse, HttpHeaders } from '@angular/common/http';
import { Observable, throwError, BehaviorSubject } from 'rxjs';
import { catchError, switchMap } from 'rxjs/operators';
import { tap } from 'rxjs/operators';

@Injectable({
  providedIn: 'root',
})
export class ApiService {
  private baseUrl = 'http://127.0.0.1:8000/api'; // Base URL de tu API
  private accessToken: string | null = null;
  private refreshToken: string | null = null;
  private isAuthenticatedSubject = new BehaviorSubject<boolean>(this.getAuthState());
  public isAuthenticated$: Observable<boolean> = this.isAuthenticatedSubject.asObservable();


  constructor(private http: HttpClient) {
    this.loadTokens();
  }

  // cargamos los token para q los datos del perfil no desaparezcan
  private loadTokens() {
    this.accessToken = localStorage.getItem('access_token');
    this.refreshToken = localStorage.getItem('refresh_token');
  }

  private saveTokens(access: string, refresh: string) {
    localStorage.setItem('access_token', access);
    localStorage.setItem('refresh_token', refresh);
    this.accessToken = access;
    this.refreshToken = refresh;
  }

  private refreshAccessToken(): Observable<any> {
    const refreshToken = localStorage.getItem('refresh_token');
    if (!refreshToken) {
      throw new Error('No se encontró el refresh token.');
    }

    return this.http.post(`${this.baseUrl}/token/refresh/`, { refresh: refreshToken }).pipe(
      tap((res: any) => {
        if (res.access) {
          localStorage.setItem('access_token', res.access); // Guarda el nuevo token
        }
      })
    );
  }

  private handle401Error(request: any): Observable<any> {
    return this.refreshAccessToken().pipe(
      switchMap((res: any) => {
        this.saveTokens(res.access, this.refreshToken!);
        const headers = new HttpHeaders({
          Authorization: `Bearer ${this.accessToken}`,
        });
        return this.http.request(request.method, request.urlWithParams, {
          body: request.body,
          headers: headers,
        });
      })
    );
  }

  private handleRequest<T>(request: any): Observable<T> {
    const headers = new HttpHeaders({
      Authorization: `Bearer ${this.accessToken}`,
    });

    return this.http.request<T>(request.method, request.urlWithParams, {
      body: request.body,
      headers: headers,
    }).pipe(
      catchError((error: HttpErrorResponse) => {
        if (error.status === 401) {
          return this.handle401Error(request);
        }
        return throwError(error);
      })
    );
  }

  // login
  login(email: string, password: string): Observable<any> {
    const data = { email, password };
    return this.http.post(`${this.baseUrl}/login/`, data); // Asegúrate de que sea un Observable
  }


  // registro
  register(data: any): Observable<any> {
    return this.http.post(`${this.baseUrl}/registro/estudiante/`, data);
  }

  // listar practicas
  getPracticas(token: string): Observable<any> {
    const headers = new HttpHeaders({
      Authorization: `Bearer ${token}`,
    });
    return this.http.get(`${this.baseUrl}/practicas/`, { headers });
  }

  getPracticaById(practicaId: number): Observable<any> {
    return this.http.get(`${this.baseUrl}/practicas/${practicaId}/`);
  }


  // detalles de 1 anuncio
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

    if (!token) {
      return throwError('No se encontró el token de acceso.');
    }

    const headers = new HttpHeaders({
      Authorization: `Bearer ${token}`,
    });

    return this.http.get(`${this.baseUrl}/postulaciones/`, { headers }).pipe(
      catchError((error) => {
        if (error.status === 401) {
          return this.refreshAccessToken().pipe(
            switchMap(() => this.getPostulaciones()) // Reintenta después de renovar el token
          );
        }
        return throwError(error);
      })
    );
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


  getComunas2(): Observable<any> {
    return this.http.get(`${this.baseUrl}/api/get-comunas`);
  }

  getCarreras(): Observable<any> {
    return this.http.get(`${this.baseUrl}/carreras/`);
  }

  getPerfil(): Observable<any> {
    const url = `${this.baseUrl}/estudiante/detail/`;
    const headers = new HttpHeaders({
      Authorization: `Bearer ${this.accessToken}`,
    });
    return this.http.get(url, { headers }).pipe(
      catchError((error: HttpErrorResponse) => {
        if (error.status === 401) {
          return this.handle401Error({ method: 'GET', urlWithParams: url });
        }
        return throwError(error);
      })
    );
  }

  getAnuncios(): Observable<any> {
    return this.http.get(`${this.baseUrl}/practicas/`);
  }

  postular(anuncioId: number, token: string): Observable<any> {
    const headers = new HttpHeaders({
      Authorization: `Bearer ${token}`,
    });
    return this.http.post(`${this.baseUrl}/postulacion/`, { anuncio_id: anuncioId }, { headers });
  }

  verificarPostulacion(anuncioId: number): Observable<{ postulado: boolean }> {
    const token = localStorage.getItem('access_token');
    const headers = new HttpHeaders({
      Authorization: `Bearer ${token}`,
    });
    return this.http.get<{ postulado: boolean }>(`${this.baseUrl}/verificar_postulacion/${anuncioId}/`, { headers });
  }

  isAuthenticated(): boolean {
    return !!localStorage.getItem('access_token');
  }

  private getAuthState(): boolean {
    return !!localStorage.getItem('access_token');
  }

  updatePerfil(data: FormData): Observable<any> {
    const token = localStorage.getItem('access_token');
    const headers = new HttpHeaders({
      Authorization: `Bearer ${token}`,
    });
    return this.http.put(`${this.baseUrl}/estudiante/update/`, data, { headers });
  }

}


