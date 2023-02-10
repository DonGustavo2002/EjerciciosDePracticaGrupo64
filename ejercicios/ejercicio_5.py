# De ºC a ºF: se multiplica por 1.8 y se suma 32.
#De ºF a ºC: se resta 32 y se divide entre 1.8.

#17 * 1.8 + 32
#79.0

def farenjeit_a_celsius(temperatura):
    return (temperatura - 32) / 1.8


temperatura_c = farenjeit_a_celsius(20)
print(f'La temperatura en ºC es: {temperatura_c}')

temperatura_c = farenjeit_a_celsius(62)
print(f'La temperatura en ºC es: {temperatura_c}')