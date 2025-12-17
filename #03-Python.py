### Estructuras ###

# Listas

my_list = ["David", "Escobedo", "darkfenris", 52, 1.79]
my_other_list = [20, 52, 30, 28, 45, 52, 18]

print(len(my_list)) # len nos indica el número de elementos de la lista
print(type(my_list)) # type nos indica la clase, en este caso clase list
print(my_list[0]) # Accedemos al valor en la posición indicada
print(my_other_list.count(52)) # count indica las veces que está el elemento indicado en la lista

my_list.append("descobedoc@gmail.com") # append añade un elemento al final de la lista
print(my_list)

my_list.insert(3, "Verde") # insert añade un elemento en la posición indicada
print(my_list)

my_list[3] = "Azul" # Se asigna un valor a una posición determinada, modificando el valor existente
print(my_list)

my_list.remove("Azul") # remove borra el elemento indicado
print(my_list)

my_other_list.pop
print(my_other_list)