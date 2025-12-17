### Estructuras ###

# Listas

my_list = ["David", "Maribel", "Joel", "Oriol"]

print(len(my_list)) # len nos indica el número de elementos de la lista
print(type(my_list)) # type nos indica la clase, en este caso clase list
print(my_list[0]) # Accedemos al valor en la posición indicada

my_list.append("Kira") # append añade un elemento al final de la lista
print(my_list)

my_list.insert(3, "Oddie") # insert añade un elemento en la posición indicada
print(my_list)

my_list[3] = "Gia" # Se asigna un valor a una posición determinada, modificando el valor existente
print(my_list)

my_list.remove("Gia") # remove borra el elemento indicado
print(my_list)

my_list.sort()
print(my_list)
