lista = [8,45,99,108,33,9,12,58,22,72,14,82,49,1]
mayor = None
menor = None
for num in lista:
    if menor == None and mayor ==None:
        menor = num
        mayor = num
    else:
        if num < menor:
            menor = num
        if num > mayor:
            mayor = num
print("El numero mayor de la lista es {mayor}")
print("El numero menor de la lista es {menor}")


