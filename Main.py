# Crear una class Personaje que tenga un atributo 
# Nombre, Vida, Fuerza y Oro

# El nombre del personaje debe ser proporcionado por el usuario
# Pero su Vida y Fuerza comenzar en 100 y su Oro en 1000

# Crear 2 personajes y mostrar sus Stats

import os
os.symtem("cls")

class Personaje:
    Nombre = ""
    Vida = ""
    Fuerza = ""
    Oro = ""

    def __init__(self, nombre:str):
        self.Nombre = nombre.title()
        self.Vida = 100
        self.Fuerza = 100
        self.Oro = 1000

    def getStats(self):
        return f"Nombre: {self.Nombre}, Vida: {self.Vida}, Fuerza: {self.Fuerza}, Oro: {self.Oro}"



Player1 = Personaje("Player 1")
Player2 = Personaje("Player 2")

print(Player1.getStats())
print(Player2.getStats())