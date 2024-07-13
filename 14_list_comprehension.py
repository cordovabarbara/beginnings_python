## List Comprehension ##

'''Las comprensiones de listas ofrecen una manera concisa de crear listas. Sus usos comunes son para hacer nuevas listas donde cada elemento es el resultado de algunas operaciones aplicadas a cada miembro de otra secuencia o iterable, o para crear un segmento de la secuencia de esos elementos para satisfacer una condición determinada.'''

my_original_list = [35, 20, 12, 45, 77, 80]

my_list = [ i for i in my_original_list]
print(my_list)

my_list = [ i + 1 for i in my_original_list]
print(my_list)

my_list = [ i* i for i in range(8)]
print(my_list)

'''ejercicio:, de la siguiente lista, devuelve una lista de numeros pares'''

numbers_list = [1,8,4,5,6,9,10,70,511,44,22]
pair_numbers_list = []
for number in numbers_list:
    if number % 2 == 0:
        (pair_numbers_list.append(number))
        print(pair_numbers_list)

##lista de compresion##

pair_numbers =[number for number in numbers_list if number % 2 == 0]
print(pair_numbers)

'''Una fórmula sencilla para escribir en forma de lista de comprensión es:

mi_lista = [{operacion con entrada n} for n in {python iterable}]'''
