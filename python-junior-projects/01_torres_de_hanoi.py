"""Algoritmo Torres de Hanoi con recursividad.
"""

def mover_disco(desde,hacia,disco):
    print(f"mover disco {disco} de la torre {desde} hacia la torre {hacia}")

def torres_de_hanoi(n,origen,destino,auxiliar):
    if n == 1:
        print("Mover disco 1 de",origen,"a",destino)
        return
    torres_de_hanoi(n-1,origen,auxiliar,destino)
    print("mover disco de",origen,"a",destino)
    torres_de_hanoi(n-1,auxiliar,destino,origen)


if __name__ == "__main__":
    torres_de_hanoi(4,"origen","destino","auxiliar")
