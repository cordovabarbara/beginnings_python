## Loops ##

# While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else:
    print("Mi condicion es mayor o igual a 10")

print("la ejecucion continua")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Mi condicion es 15, se detiene")
        break
    
