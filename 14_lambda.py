##Una función anónima de una línea consistente en un sola expression que es evaluada 
# cuando la función es llamada. 
# La sintaxis para crear una función lambda es lambda [parameters]: expression##

sum_two_values = lambda first_value, second_value: first_value + second_value
print(sum_two_values(2,8))