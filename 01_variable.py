#Variables
my_variable ='My String Variable'
print(my_variable)

my_int_variable = 5
print(my_int_variable)

is_married = True
print(is_married)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

#Concatenacion  de variables en un print
print(my_variable,(my_int_variable))
print('Este es el valor de:', is_married)

#Funcion del sistema
print(len(my_variable))

#Variables en una sola linea ¡no abusar!
name, surname, alias, age = "Barbara", "Cordova", "Barby", 31
print("Me llamo:",name, surname,".Mi edad es:",age,".Y mi alias es", alias)

#Inputs
"""
first_name = input('What is your name: ')
age = input('How old are you? ')

print(first_name)
print(age)

tipar no funciona, las variables  pueden cambiar el valor
"""