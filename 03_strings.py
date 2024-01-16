#Strings#
my_string = "Mi string"
my_other_string = "Mi otro string"

print(len(my_string))

my_new_line_string = "\teste es un string con tabulacion"
print(my_new_line_string)

#Formateo
name, surname, age = "Barbara", "Cordova", 31
print("Mi nombre es {} {} y mi edad es {}". format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))