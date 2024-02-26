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

print(len(my_dict))