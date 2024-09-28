import { ProductoConID } from './producto'
import { UsuarioConID } from './usuario'

export interface productoConCantidad {
  producto: ProductoConID;
  cantidad: number;
}

export interface Carrito {
  id: number;
  productos: Array<productoConCantidad>;
  usuario: UsuarioConID;
}
