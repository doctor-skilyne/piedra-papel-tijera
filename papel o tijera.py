
import random

PIEDRA = 1
PAPEL = 2
TIJERA = 3
SALIR = 0
array_gameOptiones  = ["", "piedra", "papel", "tijera"]
def obtener_opcion_usuario():
    while True:
        try:
            opcion = int(input("Ingrese el número correspondiente para jugar: "))
            if opcion in [PIEDRA, PAPEL, TIJERA, SALIR]:
                return opcion
            else:
                print("Número inválido. Por favor, intente de nuevo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")

def obtener_opcion_computador():
    return random.choice([PIEDRA, PAPEL, TIJERA])

def determinar_ganador(usuario, computador):
    if usuario == computador:
        return "Es un empate chale!"
    elif (usuario == PIEDRA and computador == TIJERA) or \
        (usuario == PAPEL and computador == PIEDRA) or \
        (usuario == TIJERA and computador == PAPEL):
         return "¡Ganaste! muajajaja  "
    else:
        return "Perdiste pipipi ¡Inténtalo de nuevo!"
def jugar():
    print(" Piedra, papel o tijera")
    print(f" [{PIEDRA}] piedra")
    print(f" [{PAPEL}] papel")
    print(f" [{TIJERA}] tijera")
    print(f" [{SALIR}] salir")
    while True:
        opcion_usuario = obtener_opcion_usuario()
        if opcion_usuario == SALIR:
            break
        opcion_computador = obtener_opcion_computador()
        print(f"\nHas elegido: {array_gameOptiones
		[opcion_usuario]}")
        print(f"Computador eligió: {array_gameOptiones
		[opcion_computador]}")

        resultado = determinar_ganador(opcion_usuario, opcion_computador)
        print(f"\n{resultado}")

        continuar = input("\n¿Quieres seguir jugando? (s/n): ")
        if continuar.lower() != 's':
            break

jugar()
