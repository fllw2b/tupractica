export interface Usuario {
  nombreusuario: string,
  email: string,
  contrasena: string
}
export interface UsuarioConID extends Usuario {
  usuario: string
}
export interface UsuarioParcial extends Partial<Usuario>{

}
