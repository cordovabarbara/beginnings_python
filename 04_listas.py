# Listas #

#lista es una caja para agregar, agrupar datos#


my_list = [35, 24, 31, 30, 18, 30]

print(len(my_list))

my_data = [31, 1.68, "Barbara", "Cordova"
]

print(type(my_data))
print(my_data[0])
print(my_data[-3])
print(my_data[2])
print(my_data.count("Barbara")) 
#el metodo count cuenta las ocurrencias de un valor#

age, height, name, surname = my_data
print(age)

my_list = "Hola Python"
print(my_list)

my_data.append("Continuum") #append inserta un dato al final
print(my_data)

my_data.insert(1, "altura")
print(my_data) #insert te dice agrega un valor en el index y que es lo que quieres agregar

my_data[1] = "Negro"
print(my_data) # para modificar el valor con el indice 

my_data.remove("Negro")
print(my_data)

my_data.pop(4)
print(my_data)

del my_data[1]
print(my_data) #borra por indice

my_new_list = my_data.copy()

my_data.clear()
print(my_data)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)




