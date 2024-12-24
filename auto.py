import os, subprocess
def ejecutar_comando_en_nueva_ventana(comando):
    try:
        subprocess.run(f"start cmd /k \"{comando}\"", shell=True) #/k para que no cierre la ventana y c para que cierre
    except Exception as e:
        print(f"Error al ejecutar el comando: {e}")
def mostrar_menu():
    print("\n--- Administrador del Proyecto ---\n1. Integrar cambios de github\n2. Migrar Base de Datos\n3. Iniciar el Servidor (runserver)\n4. AutoProd (git add, commit, push)\n4. Reiniciar cambios (git add, commit, push)\n6. Salir")
def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción:  ")
        os.system("cls")
        if opcion == "1":
            print("Integrando cambios")
            ejecutar_comando_en_nueva_ventana("git pull Portafolio main")
        elif opcion == "2":
            print("Ejecutando migraciones de la base de datos...")
            ejecutar_comando_en_nueva_ventana("python manage.py makemigrations && python manage.py migrate")
        elif opcion == "3":
            print("Iniciando el servidor de desarrollo...")
            ejecutar_comando_en_nueva_ventana("python manage.py runserver")
            ejecutar_comando_en_nueva_ventana("start http://127.0.0.1:8000")
        elif opcion == "4":
            print("Ejecutando AutoProd (git add, commit y push)...")
            ejecutar_comando_en_nueva_ventana("git add . && git commit -m \"Actualización desde AutoProd\" && git push origin web")            
        elif opcion == "5":
            print("Ejecutando reset")
            ejecutar_comando_en_nueva_ventana("git reset --hard HEAD")
        elif opcion == "6":
            print("Saliendo del administrador del proyecto. ¡Adiós!")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 4.")
if __name__ == "__main__":
    main()