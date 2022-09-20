from Model.Personaje import *
import os

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

    input("Presiona Enter para continuar!")
    if Turno == 1: Turno = 2
    else: Turno = 1
