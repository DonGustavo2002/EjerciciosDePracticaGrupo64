 #Escribir una función que calcule el área de un círculo dado su radio"

  #Calculo sera el area = pi*r / 2"

 #Con la libreria math with pi only"

from math import pi

R = float (input("Valor del radio: "))
AREA = pi * R ** 2
print("El Area Circulo es igual a {:.2f}".format(AREA))
