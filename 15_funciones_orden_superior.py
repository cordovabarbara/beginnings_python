'''son funciones que pueden tomar otras funciones como argumentos y/o devolver funciones como resultados. Estas funciones son una característica poderosa en programación funcional y permiten un alto grado de flexibilidad y reutilización de código'''

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_values_add_value(first_value, second_values, f_sum):
    return f_sum(first_value + second_values)

print(sum_two_values_add_value(5, 2, sum_one))
print(sum_two_values_add_value(5, 2, sum_five))