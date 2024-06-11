# Manejo de errores #

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


try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except:
    print('Something went wrong')

# Execpciones por tipo