# Operaciondes con cadenas de caracteres

s1 = "David"
s2 = "Escobedo"

# Concatenación
print(s1 + " " + s2)

# Repetición
print(s1 * 3)

# Indexación
print(s1[2])

# Longitud
print(len(s2))

# Slicing
print(s2[2:6])
print(s2[2:])
print(s2[:4])

# Búsqueda
print("a" in s1)
print("a" in s2)

# Reemplazo
print(s1.replace("a", "o"))

# División
print(s2.split("b"))

# Mayúsculas, minúsculas y letras en mayúsculas
print(s1.upper())
print(s1.lower())
print("david escobedo".title())
print("david escobedo".capitalize())