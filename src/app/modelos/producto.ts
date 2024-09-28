export interface Producto {
  nombre: string;
  foto: string;
  descripcion: string;
  cpu: string;
  gpu: string;
  ram: number;
  almacenamiento: number;
  precio: number;
  perifericos: boolean;
  fuentePoder: number;
}
export interface ProductoConID extends Producto {
  id: number;
}

export interface ProductoParcial extends Partial<Producto>{

}
