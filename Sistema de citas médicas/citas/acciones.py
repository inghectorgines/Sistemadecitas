import citas.cita as modelo


class Acciones:

    def crear(self, usuario):
        print(f"OK {usuario[1]}, Se creara una nueva consulta")

        paciente = input("Por favor introdusca el nombre del paciente: ")
        descripcion = input("Escriba la descripcion de la cita ó consulta: ")
        horaAtencion = input("Escriba el horario de antencion: ")
        costo = input("Escriba el costo: ")
        cita = modelo.Cita(usuario[0], paciente,
                           descripcion, horaAtencion, costo)
        guardar = cita.guardar()

        if guardar[0] >= 1:
            print(f"\nUsted ha agendado la cita de {paciente}")
        else:
            print(f"\nLa cita no ha sido agendada  {usuario[1]}")

    def mostrar(self, usuario):
        print(f"\n{usuario[1]} Estas son todas las consultas")
        cita = modelo.Cita(usuario[0])
        citas = cita.listar()
        # print(notas)
        for cita in citas:
            print("\n***********************")
            print(cita[2])
            print(cita[3])
            print("\n***********************")

    def modificar(self, usuario):
        print(f"\n{usuario[1]} Editar cita ")
        print("Introdusca los nuevos datos")

        Paciente = input("Introdusca el nombre del paciente: ")
        Descripcion = input("Escriba la descripcion de la cita ó consulta: ")
        HoraAtencion = input("Escriba el horario de antencion: ")
        Costo = input("Escribe el costo: ")
        cita = modelo.Cita(usuario[0], Paciente,
                           Descripcion, HoraAtencion, Costo)
        modificar = cita.modificar()

    def borrar(self, usuario):
        print(f"\n{usuario[1]} !Usted esta por eliminar la cita!")

        paciente = input("Introdusca el nombre del o la paciente ")
        cita = modelo.Cita(usuario[0], paciente)
        eliminar = cita.eliminar()
        if eliminar[0] >= 1:
            print(f"La cita se ha eliminado con exito (Y)")
        else:
            print("No se pudo eliminar la cita, intentelo más tarde")
