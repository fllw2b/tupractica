export interface Usuario {
  nombreusuario: string,
  email: string,
  contrasena: string//,
  //isAdmin: boolean
}
export interface UsuarioConID extends Usuario {
  usuario: string
}
export interface UsuarioParcial extends Partial<Usuario>{

}
