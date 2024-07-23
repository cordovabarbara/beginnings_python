'''son funciones que pueden tomar otras funciones como argumentos y/o devolver funciones como resultados. Estas funciones son una característica poderosa en programación funcional y permiten un alto grado de flexibilidad y reutilización de código'''

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