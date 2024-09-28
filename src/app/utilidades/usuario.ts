import * as CryptoJS from 'crypto-js';

export function Encriptar(texto: string): string {
  const hash = CryptoJS.SHA256(texto);
  return hash.toString(CryptoJS.enc.Hex);
}

export function obtenerDatosUsuario(){
    const usuario= localStorage.getItem('nombreusuario')
    if(!usuario){
      this.router.navigate(['']);
      }
      else
      {
        this.apiUsuario.buscarPorID(+usuario)
        .subscribe(usuarioactivo => {
          if(usuarioactivo){
            this.UsuarioLogeado = usuarioactivo;
          }else{
            localStorage.removeItem('nombreusuario');
            this.router.navigate(['']);
          }
        })
    }
  }

export function  cerrarSession(){
    const usuario= localStorage.getItem('nombreusuario')
    if(!usuario){
      this.router.navigate(['']);
      }
      else
      {
          localStorage.removeItem('nombreusuario');
          this.router.navigate(['']);
      }
    }