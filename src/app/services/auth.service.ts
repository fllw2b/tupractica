import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  private baseUrl = 'http://127.0.0.1:8000/api';

  constructor(private http: HttpClient) {}

  login(email: string, password: string): Observable<any> {
    return this.http.post(`${this.baseUrl}/login/`, { email, password });
  }

  register(data: any): Observable<any> {
    return this.http.post(`${this.baseUrl}/registro/estudiante/`, data);
  }

  refreshToken(refresh: string): Observable<any> {
    return this.http.post(`${this.baseUrl}/token/refresh/`, { refresh });
  }
}
