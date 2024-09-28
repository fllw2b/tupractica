import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { Router, ActivatedRoute } from '@angular/router';
import { CrudService } from "./../../../servicios/crud.service"
import { ProductoConID } from "../../../modelos/producto"
// cosas de filtrar usuario
import { UsuarioService } from "../../../servicios/usuario.service"
import { UsuarioConID } from "../../../modelos/usuario"

@Component({
  selector: 'app-modificar',
  templateUrl: './modificar.page.html',
  styleUrls: ['./modificar.page.scss'],
})
export class ModificarPage implements OnInit {
  // cosas de filtrar usuario
  public UsuarioLogeado: UsuarioConID;
  public esAdmin: boolean = false;

  public idActiva = 0;
  public productoActivo!: ProductoConID;
  public ram: Array<number> = [
    4,
    8,
    16,
    32
  ]

  public watts: Array<number> = [
    400,
    500,
    650,
    800
  ]

  public almacenamiento: Array<number> = [
    240,
    500,
    1000,
    2000
  ]

  public imagenBase: string = '';

  public formulario: FormGroup;

  constructor(
    private fb: FormBuilder,
    private crudServicio: CrudService,
    private router: Router,
    private rutaActiva: ActivatedRoute,
    // cosas de filtrar usuario
    private apiUsuario: UsuarioService,
  ) {
    this.formulario = this.fb.group({
      id: [0, [
        Validators.required
      ]],
      nombre: ['', [
        Validators.required,
        Validators.minLength(3),
        Validators.maxLength(20),
      ]],
      foto: ['', Validators.required],
      descripcion: ['', [
        Validators.required,
        Validators.minLength(5),
        Validators.maxLength(50),
      ]],
      cpu: ['', [
        Validators.required,
        Validators.minLength(5),
        Validators.maxLength(20)
      ]],
      gpu: ['', [
        Validators.required,
        Validators.minLength(5),
        Validators.maxLength(20)
      ]],
      ram: [0, Validators.required],
      almacenamiento: [0, Validators.required],
      precio: [0, [
        Validators.required,
        Validators.min(1),
        Validators.max(10000000)
      ]],
      perifericos: [0],
      fuentePoder: [0, [
        Validators.required,
        Validators.min(400),
        Validators.max(1200)
      ]],
    })
  }

  // MANEJO DE ERRORES
  public campo(control: string) {
    return this.formulario.get(control);
  }
  public errores(control: string) {
    return this.campo(control).errors
  }
  public esTocado(control: string) {
    return this.campo(control).touched;
  }
  public estaSucio(control: string) {
    return this.campo(control).dirty;
  }

  public guardarProducto() {
    if (this.formulario.invalid) {
      this.formulario.markAllAsTouched();
      return;
    }
    this.crudServicio.modificarPorID(this.idActiva, {
      ...this.formulario.value,
      foto: this.imagenBase
    })
      .subscribe(dato => {
        if (dato) {
          alert("Producto modificado correctamente");
          this.formulario.reset();
          this.formulario.updateValueAndValidity();
          this.router.navigate(['../listar']);
        }
      })
  }

  public cambiarFoto(e: Event) {
    const elemento = e.target as HTMLInputElement;
    const archivo = elemento.files[0];
    const reader = new FileReader();
    reader.readAsDataURL(archivo);
    reader.onload = () => {
      // BASE 64
      // console.log(reader.result);
      this.imagenBase = reader.result as string;
    }
  }

  ngOnInit() {
    this.rutaActiva.paramMap.subscribe(parametros => {
      this.idActiva = +parametros.get('id');
      this.crudServicio.buscarPorID(this.idActiva)
        .subscribe(productos => {
          if (productos) {
            this.productoActivo = productos;
            this.imagenBase = productos.foto;
            this.formulario.setValue({
              ...this.productoActivo
            });
            this.formulario.updateValueAndValidity();
          } else {
            this.router.navigate(['../listar']);
          }
        });
    })
  }



  // cosas de filtrar usuario (unico pa admin)
  ionViewDidEnter() {
    this.obtenerDatosUsuario();
  }
  public obtenerDatosUsuario() {
    const usuario = localStorage.getItem('usuario')
    if (!usuario) {
      this.router.navigate(['']);
    }
    else {
      this.apiUsuario.buscarPorID(+usuario)
        .subscribe(usuarioactivo => {
          if (usuarioactivo) {
            this.UsuarioLogeado = usuarioactivo;
            //this.esAdmin = this.UsuarioLogeado.isAdmin;
            this.pestaniaAdministrativa();
          } else {
            localStorage.removeItem('usuario');
            this.router.navigate(['']);
          }
        })
    }
  }
  public soyadmin() {
    if (this.esAdmin) {
      return true;
    }
    else {
      return null;
    }
  }
  public pestaniaAdministrativa() {
    if (this.esAdmin) {
      return true;
    }
    else {
      localStorage.removeItem('usuario');
      this.router.navigate(['']);
    }
  }

}
