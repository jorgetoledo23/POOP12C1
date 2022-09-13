from io import UnsupportedOperation
import os
os.system("cls") #=> limpiar Consola

class Cliente:
    Rut = None
    Nombres = None
    Apellidos = None
    MayorEdad = None

    #Metodo Constructor
    def __init__(self, rut, nombres:str, apellidos:str, edad:int):
        self.Rut = rut
        self.Nombres = nombres.title()
        self.Apellidos = apellidos.title()

        if edad >= 18: self.MayorEdad = True
        else: self.MayorEdad = False



    def getInfo(self):
        return f"Rut: {self.Rut}, Nombres: {self.Nombres}, Apellidos: {self.Apellidos}, Mayor Edad: {self.MayorEdad}"

ClientePedrito = Cliente("1-1", "peDRITO Alexis", "Gonzalez Fernandez", 20)
print(ClientePedrito.getInfo())

ClienteJuanito = Cliente("2-2", "juAN FERnanDo", "Farias Hernandez", 17)


ClienteJuanito.Rut = "Hola Mundo"

print(ClienteJuanito.getInfo())







