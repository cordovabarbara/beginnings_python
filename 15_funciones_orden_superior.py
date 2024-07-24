'''son funciones que pueden tomar otras funciones como argumentos y/o devolver funciones como resultados. Estas funciones son una característica poderosa en programación funcional y permiten un alto grado de flexibilidad y reutilización de código'''

from functools import reduce

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_values_add_value(first_value, second_values, f_sum):
    return f_sum(first_value + second_values)

print(sum_two_values_add_value(5, 2, sum_one))
print(sum_two_values_add_value(5, 2, sum_five))

'''Esta función toma tres argumentos: first_value, second_value y f_sum. El tercer argumento, f_sum, es una función que se aplicará al resultado de first_value + second_value.'''

#ejercicio#
'''Tienes una lista de productos con su nombre y precio. Debes realizar las siguientes tareas:
Crear dos funciones que apliquen diferentes descuentos a los precios de los productos (10% de desccuento y 20% de descuento).
Crear una función de orden superior que tome una lista de productos y una función de descuento, y aplique ese descuento a todos los productos.
Usar la función de orden superior con las funciones de descuento para obtener listas de productos con los precios descontados.'''

products = [
    {"nombre": "medias", "precio": 10.00},
    {"nombre": "hoodie", "precio": 35.00},
    {"nombre": "shirt", "precio": 40.00},
    {"nombre": "pantalon", "precio": 60.00},
    {"nombre": "sweater", "precio": 50.00},
]

def discount_ten(precio):
    #Calculas el monto del descuento y luego lo restas del precio original#
    return precio - (precio * 10 / 100)

def discount_twenty(precio): 
    return precio - (precio * 20 / 100)

def apply_discount_to_products(all_products, discount_fun):
     return [
     {"nombre": product["nombre"], "precio": discount_fun(product["precio"])}
        for product in all_products
        ]

print(apply_discount_to_products(products, discount_ten))
print(apply_discount_to_products(products, discount_twenty))

'''
products = [
    {"nombre": "medias", "precio": 10.00},
    {"nombre": "hoodie", "precio": 35.00},
    {"nombre": "shirt", "precio": 40.00},
    {"nombre": "pantalon", "precio": 60.00},
    {"nombre": "sweater", "precio": 50.00},
]

def discount_ten(price):
    return price - (price * 10 / 100)

def discount_twenty(price):
    return price - (price * 20 / 100)

def apply_discount_to_products(products, discount_fun):
    discounted_products = []  # Inicializa una lista vacía

    for product in products:
        new_price = discount_fun(product["precio"])  # Aplica el descuento
        discounted_product = {"nombre": product["nombre"], "precio": new_price}  # Crea el nuevo diccionario
        discounted_products.append(discounted_product)  # Agrega el nuevo diccionario a la lista
    
    return discounted_products

# Aplicar descuentos y imprimir resultados
print(apply_discount_to_products(products, discount_ten))
print(apply_discount_to_products(products, discount_twenty))

'''

## Closures ##
'''Un closure en Python ocurre cuando una función anidada (una función definida dentro de otra función) recuerda y puede acceder a las variables de su ámbito envolvente incluso después de que la función envolvente haya terminado de ejecutarse.'''

def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add
    
add_closure = sum_ten(1)
print(add_closure(5))

## Funciones que ya existen #

#Map necesita un conjuto iterable, itera por cada elemento y aplica la funcion#

numbers = [2, 5, 10, 21, 26, 8, 30]

def multiply(number):
    return number * 2

print(list(map(multiply,numbers)))

#Filter#

# funcion e iterable#

def filter_function(num):
    if num > 10:
        return True
    return False

print(list(filter(filter_function, numbers)))

#Reduce#
'''toma una función y una secuencia y aplica la función de manera acumulativa a los elementos de la secuencia, de modo que se reduce la secuencia a un solo valor'''

def sum_values(first, second):
    return first + second

print(reduce(sum_values, numbers ))
