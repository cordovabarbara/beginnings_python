# Funciones 

def my_function ():
    print("esto es mi funcion")

my_function()

def sum_two_values (first_number, second_number):
    print(first_number + second_number)

sum_two_values (5,7)

def other_sum (first_number, second_number):
    return first_number + second_number

my_result = other_sum(4567, 87999)
print(my_result)

def print_upper(*texts):
    for text in texts:
        print(text.upper())

print_upper ( "hola", "barbara", "bienvenido", "a", "python")

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)