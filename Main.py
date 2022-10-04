from Model.Personaje import *
import os
import Tienda


Player1 = Personaje("Player 1")
Player2 = Personaje("Player 2")
Ganador = None

Turno = 1
while True:
    os.system("cls")
    print(f"Turno Actual: {Turno}\n")
    
    print(f"Stats Player 1: {Player1.getStats()}")
    print("Inventario P1: ")
    Player1.getInventario()
    print("\n")
    
    print(f"Stats Player 2: {Player2.getStats()}")
    print("Inventario P2: ")
    Player2.getInventario()
    print("\n")

    print("[1] - Atacar")
    print("[2] - Comprar Item")
    print("[3] - Vender Item")
    jugada = input("Selecciona tu Jugada: ")

    if jugada == "1":
        #Atacar
        if Turno == 1: 
            Player1.Atacar(Player2)
            if Player2.getVida() <= 0:
                Ganador = Player1
        else: 
            Player2.Atacar(Player1)
            if Player1.getVida() <= 0:
                Ganador = Player2

    if jugada == "2":
        os.system("cls")
        indice = 1
        for item in Tienda.Tienda:
            print(f"[{indice}] - {item.getStats()}")
            indice += 1
        opcion = int(input("Que deseas Comprar?: "))

        if Turno == 1: Player1.Comprar(Tienda.Tienda[opcion - 1])
        else: Player2.Comprar(Tienda.Tienda[opcion - 1])

    if jugada == "3": #Vender
        os.system("cls")
        if Turno == 1:
            indice = 1
            for item in Player1.obtenerInvertario():
                print(f"[{indice}] - {item.getStats()}")
                indice += 1
            opcion = int(input("Que deseas Vender?: "))
            Player1.Vender(Player1.obtenerInvertario()[opcion - 1])
        else:
            indice = 1
            for item in Player2.obtenerInvertario():
                print(f"[{indice}] - {item.getStats()}")
                indice += 1
            opcion = int(input("Que deseas Vender?: "))
            Player2.Vender(Player2.obtenerInvertario()[opcion - 1])

    if Ganador != None:
        print(f"Jugador: {Ganador.getStats()} Gana el Game!!!")
        break



    input("Presiona Enter para continuar!")
    if Turno == 1: Turno = 2
    else: Turno = 1
