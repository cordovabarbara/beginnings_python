#Strings#
my_string = "Mi string"
my_other_string = "Mi otro string"

print(len(my_string))

my_new_line_string = "\teste es un string con tabulacion"
print(my_new_line_string)

#Formateo
name, surname, age = "Barbara", "Cordova", 31
print("Mi nombre es {} {} y mi edad es {}". format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))

#inferencia de datos
print(f"Mi nombre es {name} {surname} y mi edad es {age}") #mas rapida y mas util - interpolacion
print(f"Mi apellido es {surname} y mi nombre es {name}")

# Desempaquetado de caracteres  
lenguage = "python"
a,b, c, d, e, f = lenguage
print(a)
print(f)

#Division

lenguage_slice = lenguage[0:3]
print(lenguage_slice)

#reverse
reverse = lenguage [::-1]
print(reverse)

#funciones

print(lenguage.capitalize())
print(lenguage.upper())
print(lenguage.count("p"))
print(lenguage.isnumeric())
print(lenguage.lower())
print(lenguage.isupper())
print(lenguage.startswith("tho"))
print(lenguage.startswith("py"))