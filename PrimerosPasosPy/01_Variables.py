# Variables 

my_string_variable = "My string variable"
print(my_string_variable)

my_int_variable = 7
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# Concatenacion de variables en un print
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

# Algunas funciones del sistema
print(len(my_string_variable))

# Variables en una sola linea !!!! Cuidado con abusar de esta sintaxis !!!!!
name, lastname, alias, age = "Nicolas", "Diaz", "Miko", 19
print("Me llamo:", name, lastname, ".Tengo:", age,"años", "Y mi alias es:", alias)

# Inputs
'''name = input("¿Cual es tu nombre?: ")
age = input("¿Cuantos años tienes?: ")

print(name)
print(age)'
'''

# Cambiamos su tipo 
name = 35
age = "Nicolas"
print(name)
print(age)

# Forzamos el tipo?
address : str = "Mi direccion"
address = True
address = 5
address = 1.2
print(type(address))