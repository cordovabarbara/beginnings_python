##Una función anónima de una línea consistente en un sola expression que es evaluada 
# cuando la función es llamada. 
# La sintaxis para crear una función lambda es lambda [parameters]: expression##

sum_two_values = lambda first_value, second_value: first_value + second_value
print(sum_two_values(2,8))

multiply_values = lambda first, second: first * second - 3
print(multiply_values(2,4))

def sum_three_values(value): 
    return lambda first_value, second_value: first_value + second_value + value
print(sum_three_values(5)(2,4))

'''Ejercicio:
Crea una lista de diccionarios llamada productos, donde cada diccionario represente un producto con un nombre y un precio. Luego, utiliza una función lambda para filtrar los productos que tienen un precio mayor a 50 y ordenarlos de menor a mayor precio.

Instrucciones:
Crea una lista de diccionarios con al menos 5 productos, cada uno con un nombre y un precio.
Utiliza una función lambda con filter() para filtrar los productos cuyo precio sea mayor a 50.
Utiliza una función lambda con sorted() para ordenar los productos filtrados de menor a mayor precio.
Imprime la lista resultante.'''

products = [
    {"nombre": "medias", "precio":10.00},
    {"nombre": "hoodie", "precio":35.00},
    {"nombre": "shirt", "precio":40.00},
    {"nombre": "pantalon", "precio":60.00},
    {"nombre": "sweater", "precio":50.00},
]
'''filter(func, iterable)'''
higher_priced_products = list(filter(lambda product: product["precio"] > 50, products))
print(higher_priced_products)



