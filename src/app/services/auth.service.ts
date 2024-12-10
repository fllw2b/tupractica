import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BehaviorSubject, Observable } from 'rxjs';
import { tap } from 'rxjs/operators';

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  private baseUrl = 'http://127.0.0.1:8000/api';

  // BehaviorSubject para el estado de autenticación
  private isAuthenticatedSubject = new BehaviorSubject<boolean>(this.getAuthState());
  public isAuthenticated$: Observable<boolean> = this.isAuthenticatedSubject.asObservable();

  constructor(private http: HttpClient) {}

  // Método para iniciar sesión
  login(email: string, password: string): Observable<any> {
    return this.http.post(`${this.baseUrl}/login/`, { email, password }).pipe(
      tap((res: any) => {
        if (res.access && res.refresh) {
          localStorage.setItem('access_token', res.access);
          localStorage.setItem('refresh_token', res.refresh);
          this.isAuthenticatedSubject.next(true); // Actualiza el estado de autenticación
        }
      })
    );
  }

  // Método para cerrar sesión
  logout() {
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    this.isAuthenticatedSubject.next(false); // Actualiza el estado de autenticación
  }

  // Método para verificar si el usuario está autenticado
  isAuthenticated(): boolean {
    const token = localStorage.getItem('access_token');
    return !!token; // Devuelve true si el token existe, false de lo contrario
  }

  // Método para registrar un usuario
  register(data: any): Observable<any> {
    return this.http.post(`${this.baseUrl}/registro/estudiante/`, data);
  }

  // Método para refrescar el token de acceso
  refreshToken(): Observable<any> {
    const refresh = localStorage.getItem('refresh_token');
    if (!refresh) {
      throw new Error('No refresh token available');
    }
    return this.http.post(`${this.baseUrl}/token/refresh/`, { refresh }).pipe(
      tap((res: any) => {
        if (res.access) {
          localStorage.setItem('access_token', res.access);
          this.isAuthenticatedSubject.next(true); // Actualiza el estado si el token se refrescó
        }
      })
    );
  }

  public getAuthState(): boolean {
    return !!localStorage.getItem('access_token');
  }


}
