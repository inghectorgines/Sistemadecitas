from ast import alias
from statistics import mode
import usuarios.usuario as modelo
import citas.acciones
from datetime import datetime


class Acciones:
    def registro(self):
        print("Por favor registrate en el sistema")

        nombre = input("Nombre: ")
        apellidos = input("Apellidos: ")
        noConsultorio = input("Numero de consultorio: ")
        email = input("Email: ")
        password = input("Introduce una contraseña: ")

        usuario = modelo.Usuario(
            nombre, apellidos, noConsultorio, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(
                f"\nBienvenido {registro[1].nombre} tu registro ha sido exitoso")
        else:
            print("\nError al registrarte, por favor verifica la información")

    def login(self):
        print("\nLOGIN: Inicia Session")

        try:
            email = input("Introduce tu correo electronico: ")
            password = input("Introduce tu contraseña: ")

            usuario = modelo.Usuario('', '', '', email, password)
            login = usuario.identificar()
            now = datetime.now()
            if email == login[4]:
                print(f"Bienvenido {login[1]}, ingresaste en la fecha: {now}")
                self.proximasAcciones(login)

        except Exception as e:
            print("Inicio de session incorrecto, intentelo mas tarde")

    def proximasAcciones(self, usuario):
        print("""
        Aciones disponibles 
         -Agendar cita (crear)
         -Mostar citas (mostar)
         -Modificar cita (modificar)
         -Eliminar cita (eliminar)
         Salir (salir)
        """)
        accion = input("¿Que desea hacer? ")
        hazEL = citas.acciones.Acciones()

        if accion == "crear":
            hazEL.crear(usuario)
            self.proximasAcciones(usuario)

        elif accion == "mostar":
            hazEL.mostrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "modificar":
            hazEL.mostrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "eliminar":
            hazEL.borrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "salir":
            exit()
