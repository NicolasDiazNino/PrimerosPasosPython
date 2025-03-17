### Lists ###

# Definicion

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [19, 24, 35, 18, 35, 20, 36]

print(my_list)
print(len(my_list))

my_other_list = [19, 1.75, "Nicolas", "Diaz"]

print(type(my_list))
print(type(my_other_list))

# Acceso a elementos y busquedas

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
print(my_list.count(35))

#print(my_other_list[4])  IndexError: sobre pasa el rango de la lista
#print(my_other_list[-5])  IndexError: sobre pasa el rango de la lista

age, height, name, lastname = my_other_list
print(name)

name, height, age, lastname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)

# Concatenacion

print(my_list + my_other_list)
#print(my_list - my_other_list)   IndexError

# Creacion, insercion, actualizacion y eliminacion

my_other_list.append("MikosGym")
print(my_other_list)

my_other_list.insert(1, "Negro")
print(my_other_list)

my_other_list[1] = "Beich"
print(my_other_list)

my_other_list.remove("Beich")
print(my_other_list)

my_list.remove(35)   # el remove elimina datos especificos, si hay mas de uno elimina el primero que encuentra
print(my_list)

print(my_list.pop())
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

del my_list[2]   # el comando del elimina por indice en la lista
print(my_list)

# Operaciones con listas

my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

#Sublistas

print(my_new_list[1:3])

# Cambio e tipo

my_list = "Hola Python"
print(my_list)
print(type(my_list))