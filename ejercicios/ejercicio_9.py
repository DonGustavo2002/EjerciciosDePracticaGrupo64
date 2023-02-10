#. Crear un programa que genere una matriz de números y la imprima en pantalla
from random import randint
def generar_matriz(n):
    matriz = []

    for m in range(n):
        fila = []

        for x in range(n):
            fila.append(randint(1, 50))

        matriz.append(fila)

    return matriz


resultado = generar_matriz(8)

print(resultado)