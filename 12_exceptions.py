# Manejo de errores #
"""""
numberOne = 5
numberTwo = 1
numberTwo = "1"

try:
    print(numberOne + numberTwo )
    print("No se ha producido un error")
except:
    print("se ha producido un error")
else:
    print ("La ejecucion continua") #esto se ejecuta si no se produce un excepcion
""""""

##  manejo de errores y el tipo de error

try:
    print(numberOne + numberTwo )
    print("No se ha producido un error")
except TypeError:
    print("se ha producido un TypError")

try:
    numero = int(input("Introduce un numero: "))
    resultado = 10 / numero
except ValueError:
    print("Error: Debes introducir un numero entero")
except ZeroDivisionError:
    print("Error: Division por cero")
    


Conceptos Básicos
try: Bloque que contiene el código que puede producir una excepción.
except: Bloque que se ejecuta si ocurre una excepción dentro del bloque try.
else: Bloque que se ejecuta si no ocurre ninguna excepción en el bloque try.
finally: Bloque que se ejecuta siempre, ocurra o no una excepción.

#Ejemplo completo
"""

def dividir ():
    try:
        numero = int(input("Introduce un numero "))
        resultado = 10 / numero
    except ValueError as valueError:
        print(f"Error de valor: {valueError}")
    except ZeroDivisionError as zeroDivision:
        print(f"Error division por 0: {zeroDivision}")
    except Exception as execption:
        print(f" Error inesperado: {execption}")
    else:
        print(f"El resultado es: {resultado}")
    finally:
        print("Fin de la operacion")
    
dividir()