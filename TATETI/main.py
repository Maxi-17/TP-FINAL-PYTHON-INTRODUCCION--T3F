from random import randrange
import os

# este tateti es para jugar contra la maquina
# randrange(lista) le podemos pasar una lista de valores para que asigne uno al azar

def limpiar():
    os.system("cls")


def crear_tablero():
    return [" " for _ in range(9)]


def mostrar_tablero(tablero):
    print ()
    print (f"{tablero[0]} | {tablero[1]} | {tablero[2]} ")
    print("--+---+--")
    print(f"{tablero[3]} | {tablero[4]} | {tablero[5]}")
    print("--+---+--")
    print(f"{tablero[6]} | {tablero[7]} | {tablero[8]}")
    print()

def hay_ganador(tablero, simbolo):
    combinaciones = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # filas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columnas
        [0, 4, 8], [2, 4, 6]              # diagonales
    ]
    for combo in combinaciones:
        if tablero[combo[0]] == tablero[combo[1]] == tablero[combo[2]] == simbolo:
            return True
    return False

def tablero_lleno(tablero):
    return " " not in tablero

def turno_usuario(tablero):
    while True:
        try:
            posicion = int(input("Elige una posicion (1-9): ")) - 1
            if 0 <= posicion < 9 and tablero[posicion] == " ":
                tablero[posicion] = "X"
                break
            else:
                print("Posicion invalida o ya esta ocupada.")
        except ValueError:
            print("Tenes que ingresar un numero del 1 al 9")

def turno_maquina(tablero):
    posiciones_libres = [i for i in range(9) if tablero[i] == " "]
    if posiciones_libres:
        posicion = randrange(len(posiciones_libres))
        tablero[posiciones_libres[posicion]] = "O"

def jugar():
    tablero = crear_tablero()
    limpiar()
    print("Bienvenido al Ta-Te-Ti! Te toca jugar con la 'X'")
    mostrar_tablero(tablero)

    while True:     
        turno_usuario(tablero)
        mostrar_tablero(tablero)
        if hay_ganador("X"):
            print("Ganaste!!")
            break
        if tablero_lleno(tablero):
            print("Empataron!!")
            break
        print("Es el turno de la maquina...")
        turno_maquina(tablero)
        mostrar_tablero(tablero)
        if hay_ganador("O"):
            print("Te gano la maquina!! :( )")
            break
        if tablero_lleno(tablero):
            print("Empataron!!")
            break

def main():
    while True:
        jugar()
        opcion = input("\nQueres jugar otra ronda? (s/n): ")
        if opcion.lower() != "s":
            print("Muchas Gracias por jugar. Hasta la proxima!")
            break

main()
