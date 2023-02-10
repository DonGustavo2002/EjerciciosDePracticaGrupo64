#Crear un programa que genere una lista de números aleatorios y los imprima en pantalla

from random import randint
numero_generico = [randint(1, 100) for _ in range(100)]
print(numero_generico)
