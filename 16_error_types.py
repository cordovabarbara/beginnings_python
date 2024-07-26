# Error Types #

# SyntaxError 

#print " Hola Comunidad"
print (" Hola Comunidad")
'''SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?'''

#NameError
#NameError: name 'variable' is not defined. Did you mean: 'callable'?
#print(variable)
variable = 5
print(variable)

# IndexError
#IndexError: list index out of range 
#print(my_list[5])
my_list =["Python", "Javascript", "C++", "Dart"]
print(my_list[3])
#print(my_list["Nombre"])
#TypeError: list indices must be integers or slices

# ModuleNotFoundError
"""import maths
ModuleNotFoundError: No module named 'maths'"""
import math

#AttributeError
#print(math.PI)
#AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?
print(math.pi)

# KeyError
#my_new_dict = {"Nombre":"Anais", "Apellido":"Cordova", "Edad":31, 1:"Python"}
#print(my_new_dict["Apellidos"])
#KeyError: 'Apellidos'
my_new_dict = {"Nombre":"Anais", "Apellido":"Cordova", "Edad":31, 1:"Python"}
print(my_new_dict["Apellido"])

#ImportError
#from math import PI
#ImportError: cannot import name 'PI' from 'math' (unknown location). Did you mean: 'pi'?
from math import pi
print(pi)

# ValueError
#my_int = int("10 años")
#print(type(my_int))
#ValueError: invalid literal for int() with base 10: '10 años'
my_int = int("10")
print(type(my_int))

# ZeroDivisionError
#ZeroDivisionError: division by zero
#print(4/0)
print(4/2)

