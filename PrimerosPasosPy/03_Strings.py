### Strings ###

my_string = "Mi string"
My_other_string = 'Mi otro string'

print(len(my_string))
print(len(My_other_string))

print(my_string + " " + My_other_string)

my_new_line_string = "Este es un String\nCon salto de linea"
print(my_new_line_string)

my_tab_string = "\t Este es un string con tabulacion"
print(my_tab_string)

my_scape_string = "\\tEste es un string \\n\\tescapado"
print(my_scape_string)

# Formateo

name, lastname, age = "Nicolas", "Diaz", 19

print("Mi nombre es %s %s y mi edad es %d" %(name, lastname, age)) 
print("Mi nombre es {} {} y mi edad es {}".format(name, lastname, age))
print("Mi nombre es " + name + " " + lastname + " y mi edad es " + str(age))
print(f"Mi nombre es {name} {lastname} y mi edad es {age}")

# Des empaquetado de caracteres

language = "Python"
a, b, c, d, e, f = language
print(a)
print(b)
print(c)
print(c)
print(e)
print(f)

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

# Reverse 

reversed_language = language[::-1]
print(reversed_language)

# Funciones

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.upper().isupper())
print(language.startswith("Py"))