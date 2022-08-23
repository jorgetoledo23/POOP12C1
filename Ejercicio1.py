class Alumno:

    Rut = ""
    Nombre = ""
    Apellido = ""
    Carrera = ""

    def __init__(self, rut, nombre, apellido, carrera):
        self.Rut = rut
        self.Nombre = nombre
        self.Apellido = apellido
        self.Carrera = carrera
    
    def getInfo(self):
        return f"Rut: {self.Rut}, Nombre: {self.Nombre}, Apellido: {self.Apellido}, Carrera: {self.Carrera}"

from Model.Sistema import *
Sis = Sistema()
Sis.Clear()

print("Sistema Escolar")
listaAlumnos = []

while(True):
    Sis.Clear()
    print("1-Ingreso Alumnos")
    print("2-Ver Listado")
    print("0-Salir")

    opcion = input("Seleccione una Opcion:")

    if(opcion == "1"):
        #Ingresar Alumnos
        rut = input("Ingrese Rut: ")
        nombre = input("Ingrese Nombre: ")
        apellido = input("Ingrese Apellido: ")
        carrera = input("Ingrese Carrera: ")

        #Crear Instancia
        A = Alumno(rut, nombre, apellido, carrera)

        #Ingresar al Listado
        listaAlumnos.append(A)

        input("Alumno Ingresado... Presione para Continuar!")

    if(opcion == "2"):
        #Ver el Listado
        for a in listaAlumnos:
            print(a.getInfo())
        input("Alumnos Listados... Presione para Continuar!")

    if (opcion == "0"):
        break