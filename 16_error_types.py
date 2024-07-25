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

# ModuleNotFoundError
"""import maths
ModuleNotFoundError: No module named 'maths'"""
import math