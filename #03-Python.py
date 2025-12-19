### Estructuras ###

# Listas

my_list: list = ["David", "Maribel", "Joel", "Oriol"]

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

# Tuplas

my_tuple: tuple = ("David", "Maribel", "Joel", "Oriol")

print(my_tuple)
print(my_tuple[1]) # Acceso a elementos de la tupla
my_tuple = tuple(sorted(my_tuple)) # Ordenación
print(my_tuple)

# Sets

my_set: set = {"David", "Maribel", "Joel", "Oriol"}

print(my_set)
my_set.add("Kira") # Añadimos un elemento al set
my_set.add("Kira") # No se pueden duplicar elementos
print(my_set)
my_set.remove("David") # Eliminamos un elemento del set
print(my_set)

# Diccionarios

my_dict: dict = {"name":"David",
                "surname":"Escobedo",
                "alias":"descobedoc", 
                "age":"52"
                }

print(my_dict)
my_dict["email"] = "descobedoc@gmail.com" # Inserción
print(my_dict)
print(my_dict["name"]) # Acceso
my_dict["age"] = "53" # Actualización
print(my_dict)
del my_dict["surname"] # Eliminación
print(my_dict)
my_dict = dict(sorted(my_dict.items()))
print(my_dict)

# Dificultad Extra

def my_agenda():

    agenda = {}

    def insert_contact():
        phone = input("Introduce el teléfono del contacto: ")
        if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
            agenda[name] = phone
        else:
            print("Debes introducir un número de teléfono con máximo 11 dígitos")

    while True:

        print(" ")
        print("1. Buscar contacto")
        print("2. Insertar contacto")
        print("3. Actualizar contacto")
        print("4. Borrar contacto")
        print("5. Salir")

        opcion = input("\nSelecciona una operación: ")

        match opcion:

            case "1":
                name = input("Introduce el nombre del contacto a buscar: ")
                if name in agenda:
                    print(f"El número de teléfono de {name} es {agenda[name]}")
                else:
                    print(f"El contacto {name} no existe.")
            case "2":
                name = input("Introduce el nombre del contacto: ")
                insert_contact()
            case "3":
                name = input("Introduce el nombre del contacto: ")
                if name in agenda:
                    insert_contact()
                else:
                     print(f"El contacto {name} no existe.")
            case "4":
                name = input("Introduce el nombre del contacto a eliminar: ")
                if name in agenda:
                    del agenda[name]
                else:
                    print(f"El contacto {name} no existe.")
            case "5":
                print("Saliendo de la agenda")
                break
            case _:
                print("Opción no válida. Escribe una opción del 1 al 5")



my_agenda()