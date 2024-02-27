##Dictionaries##
#Clave valor

my_dict = dict()
print(type(my_dict))

my_new_dict = {"Nombre":"Anais", "Apellido":"Cordova", "Edad":31, 1:"Python"}
print(my_new_dict)

my_dict = {
    "Nombre":"Anais",
    "Apellido":"Cordova", 
    "Edad":31, 
    "Lenguajes":{"Python", "Javascript", "kotlin"},
    1:1.69
}
print(my_dict)

print(my_dict["Nombre"])

my_dict["Nombre"] = "Leonor"
print(my_dict["Nombre"])  
##Se puede acceder a una clave y cambiar el valor##
print(my_dict[1])

my_dict["Direccion"] = "Bogota"
print(my_dict)

del my_dict ["Direccion"]
print(my_dict)

print("Cordova" in my_dict) ##asi se esta buscando por clave no por valor##

print("Apellido" in my_dict)

print(my_dict.items ()) #listado de casa uno de los items
print(my_dict.keys ()) #listado de keys
print(my_dict.values ()) ## retorna todos los valores

a_new_dict = my_dict.fromkeys(my_dict)
print(a_new_dict)

print(list(a_new_dict))

