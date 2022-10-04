# Crear una class Personaje que tenga un atributo 
# Nombre, Vida, Fuerza y Oro

# El nombre del personaje debe ser proporcionado por el usuario
# Pero su Vida y Fuerza comenzar en 100 y su Oro en 1000

# Crear 2 personajes y mostrar sus Stats

import os
os.system("cls")

class Personaje:

    def __init__(self, nombre:str):
        self.__Nombre = nombre.title()
        self.__Vida = 100
        self.__Fuerza = 100
        self.__Oro = 1000
        self.__Inventario = []

    def obtenerInvertario(self):
        return self.__Inventario

    def getStats(self):
        return f"Nombre: {self.__Nombre}, Vida: {self.__Vida}, Fuerza: {self.__Fuerza}, Oro: {self.__Oro}"

    def getVida(self):
        return self.__Vida

    def setVida(self, nuevaVida:int):
        self.__Vida = nuevaVida

    def Atacar(self, Objetivo):
        fuerzaGolpe = int(self.__Fuerza / 15 + 10)
        Objetivo.setVida(Objetivo.getVida() - fuerzaGolpe)

    def Comprar(self, Item):
        if self.__Oro >= Item.getCoste():
            self.__Oro -= Item.getCoste()
            self.__Vida += Item.getVida()
            self.__Fuerza += Item.getFuerza()
            self.__Inventario.append(Item)
            print("Item Comprado!")
        else:
            print("Oro Insuficiente!")

    def Vender(self, Item):
        self.__Oro += int(Item.getCoste() * 0.5)
        self.__Vida -= Item.getVida()
        self.__Fuerza -= Item.getFuerza()
        self.__Inventario.remove(Item)
        print("Item Vendido!")


    def getInventario(self):
        for item in self.__Inventario:
            print(item.getNombre()) 


