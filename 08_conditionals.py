## Condicionales
##si se cumple lo que esta en la condicion, se ejecuta la accion que esta adentro

my_condition = False

if my_condition:
    print("Se ejecuta la condicion del if")

my_condition = 5 * 3

if my_condition >= 10:
    print("Se ejecuta el segundo if")

if my_condition > 10 and my_condition < 20:
    print("Es Mayor que 10")
else:
    print("Es menor o igual que 10 o mayor o igual que 20")

print("La ejecucion continua")

##elif necesita una condicion es para hacer algo en concreto
'''En otras palabras, elif permite evaluar condiciones adicionales después de la primera if y antes de la else. Si la condición en la cláusula if no es verdadera, se verifica la primera cláusula elif, y así sucesivamente. La primera cláusula elif cuya condición sea verdadera se ejecutará y el resto de las cláusulas elif y else se ignorarán.'''

my_string = "Mi texto corto"

if my_string:
    print("Mi cadena de texto no esta vacia")

