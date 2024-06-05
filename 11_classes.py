# Classes #
#Creamos una clase para crear un objeto. Una clase es como un constructor de objetos o un "modelo" para crear objetos. Creamos una instancia de una clase para crear un objeto. La clase define los atributos y el comportamiento del objeto, mientras que el objeto, por otro lado, representa la clase.#

class Person:
    def __init__(self, name, surname, alias):
        #self.name = name
        #self.surname = surname#
        self.full_name = f"{name} {surname} ({alias}) "

    def walk (self):
        print(f"{self.full_name} esta caminado")


my_person = Person( "Barbara", "Cordova", ("Barby"))
print(my_person.full_name)
my_person.walk()
