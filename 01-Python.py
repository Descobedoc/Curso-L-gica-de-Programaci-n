# Operadores y estructuras de control

# Operadores aritméticos

print(f"Suma 3 + 4: {3 + 4}")
print(f"Resta 5 - 1: {5 - 1}")
print(f"Multiplicación 2 * 6: {2 * 6}")
print(f"División 10 / 2: {10 / 2}")
print(f"Módulo 10 % 3: {10 % 3}")
print(f"Exponente 2 ** 4: {2 ** 4}")
print(f"División entera 10 // 3: {10 // 3}")

# Operadores comparativos

print(3 < 5)
print(3 > 5)
print(3 == 5)
print(3 != 5)
print( 3<= 5)
print(3 >= 5)

# Operadores lógicos

print((3 < 4) and (5 > 2))
print((3 > 5) or (5 > 1))
print(not(5 > 2))

# Ejercicio extra

for number in range(10, 56):
    if((number %2 == 0) and (number != 16) and (number %3 != 0)):
        print(number)


