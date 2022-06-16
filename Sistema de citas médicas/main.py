## Descargo y procedo a revisar y calificar.


""" Sistema de citas médicas
1.- Abrir asistente.
2.- Login y registro.
3.- Para crear un usuario en la BD debes ir al apartado de registro.
4.- Si por el contrario decides iniciar sesión el usuario será un Doctor(a).
5.- Puedes crear, editar, mostrar y eliminar las citas.
 """

from usuarios import acciones

print("""
\n
####### BIENVENIDO #######

""")

hazEl = acciones.Acciones()


def bienvenida():

    print("""

  ¿Con que te gustaria iniciar?
  \n
  -¿Eres nuevo? (Escribe 'registro')
  \n
  -¿Ya tienes cuenta? (Escribe 'login')
  """)

    accion = input("¿Que quieres hacer?:")

    if accion == "registro":
        hazEl.registro()
        bienvenida()

    elif accion == "login":
        hazEl.login()


bienvenida()
