#Escribir una función que calcule el factorial de un número dado
def factorial (*n):
    for x in n:
        fac=1
        for y in range(1,x+1):
            fac=fac*y
        print( fac)