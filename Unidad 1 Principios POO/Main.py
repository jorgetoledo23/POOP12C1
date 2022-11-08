from Model.Personaje import *
import os
import Tienda

CantidadTurnos = 1
Player1 = Personaje("Alexis")
Player2 = Personaje("Arturo")
Ganador = None
JugadorEnTurno = Player1
JugadorEnEspera = Player2

Turno = 1
while True:
    TurnoExitoso = True
    os.system("cls")
    print(f"Jugador en Turno Actual: {JugadorEnTurno.getNombre()}\n")
    
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
    print("[4] - Rendirse")
    jugada = input("Selecciona tu Jugada: ")

    if jugada == "1":
        #Atacar
        print(f"Ataque Exitoso. Daño Inflinjido: {JugadorEnTurno.Atacar(JugadorEnEspera)}")

        if JugadorEnEspera.getVida() <= 0:
            Ganador = JugadorEnTurno

    if jugada == "2":
        os.system("cls")
        
        #Inventario Lleno
        #1-2-3-4-5
        if len(JugadorEnTurno.obtenerInvertario()) >= 6:
            input("Inventario Lleno. Presiona Enter para Continuar!")
            TurnoExitoso = False
        else:
            indice = 1
            for item in Tienda.Tienda:
                print(f"[{indice}] - {item.getStats()}")
                indice += 1
            opcion = int(input("Que deseas Comprar?: "))
            while opcion <= 0 or opcion >= len(Tienda.Tienda):
                opcion = int(input("Que deseas Comprar?: "))
            if JugadorEnTurno.Comprar(Tienda.Tienda[opcion - 1]) == 2:
                TurnoExitoso = False
            

    if jugada == "3": #Vender
        os.system("cls")
        indice = 1
        for item in JugadorEnTurno.obtenerInvertario():
            print(f"[{indice}] - {item.getStats()}")
            indice += 1
        opcion = int(input("Que deseas Vender?: "))
        JugadorEnTurno.Vender(JugadorEnTurno.obtenerInvertario()[opcion - 1])

    if jugada == "4":
        rendirse = input("Estas seguro de Rendirte? (S/N): ")
        if rendirse == "S":
            Ganador = JugadorEnEspera
        else:
            TurnoExitoso = False

    if Ganador != None:
        input(f"Jugador: {Ganador.getStats()} Gana el Game!!! en {CantidadTurnos} turnos!")
        break

    if TurnoExitoso == True:
        input("Presiona Enter para continuar!")
        CantidadTurnos += 1
        if Turno == 1: 
            Turno = 2
            JugadorEnTurno = Player2
            JugadorEnEspera = Player1
        else: 
            Turno = 1
            JugadorEnTurno = Player1
            JugadorEnEspera = Player2
