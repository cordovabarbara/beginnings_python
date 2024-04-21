## Loops ##

# While

my_condition = 0

while my_condition < 10:
    #el bucle while, itera en funcion de una condicion
    print(my_condition)
    my_condition += 2
else:
    print("Mi condicion es mayor o igual a 10")

print("la ejecucion continua")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Mi condicion es 15, se detiene")
        break
    

#For  -- itera dependiendo de la cantidad de elementos que tenga

my_list = [35, 24, 31, 30, 18, 30]

for element in my_list:
    print(element)

my_dict = {"Nombre":"Anais", "Apellido":"Cordova", "Edad":31, 1:"Python"}

for elements in my_dict:
    print(elements)
    if elements == "Edad":
        break
    print("se ejecuta")
else:
    print("El bucle For para mi diccionario a finalizado")

for elements in my_dict:
    print(elements)
    if elements == "Nombre":
        continue
    print("se ejecuta")
else:
    print("El bucle For para mi diccionario a finalizado")