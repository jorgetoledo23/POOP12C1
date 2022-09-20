from Model.Personaje import *
import os
import Tienda


Player1 = Personaje("Player 1")
Player2 = Personaje("Player 2")

Turno = 1
while True:
    os.system("cls")
    print(f"Turno Actual: {Turno}")
    
    print(f"Stats Player 1: {Player1.getStats()}")
    print(f"Stats Player 2: {Player2.getStats()}")

    print("[1] - Atacar")
    print("[2] - Comprar Item")
    jugada = input("Selecciona tu Jugada: ")

    if jugada == "1":
        #Atacar
        if Turno == 1: Player1.Atacar(Player2)
        else: Player2.Atacar(Player1)

    if jugada == "2":
        os.system("cls")
        indice = 1
        for item in Tienda.Tienda:
            print(f"[{indice}] - {item.getStats()}")
            indice += 1
        opcion = int(input("Que deseas Comprar?: "))

        if Turno == 1: Player1.Comprar(Tienda.Tienda[opcion - 1])
        else: Player2.Comprar(Tienda.Tienda[opcion - 1])
        print("Item Comprado")
        
    input("Presiona Enter para continuar!")
    if Turno == 1: Turno = 2
    else: Turno = 1
