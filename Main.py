from Model.Prenda import *
from Model.Doctor import *

#Instancia
P = Prenda()
P.Color = "Rojo"  #Asignacion
print("El Color de la Prenda es: " + P.Color) #Leer Valor

#Generar un Objeto de Tipo Doctor y LLenar su Informacion
Doctor1 = Doctor("1.111.111-1", "Genaro", "Gonzalez")
Doctor1.Rut = "1.111.111-1"
Doctor1.Nombre = "Genaro"

print(Doctor1.ObtenerInformacion())


Doctor2 = Doctor("2.222.222-2", "Alexis", "Sanchez")
Doctor2.Rut = "2.222.222-2"
print(Doctor2.ObtenerInformacion())


