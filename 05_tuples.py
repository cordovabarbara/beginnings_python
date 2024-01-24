# Tuples #
my_tuple = tuple()
my_other_tuple = ()

my_tuple = (31, 1.68, "Cordova", "Barbara")

my_other_tuple = (30, 45, 50, 25)

print(type(my_tuple))
print(my_tuple[0])
print(my_tuple[-4])

print(my_tuple.count("Cordova"))
print(my_tuple.index("Barbara"))

#y_tuple[1] = 1.80
#print(my_tuple)
##tupla no son mutables

my_sum = my_tuple + my_other_tuple
print(my_sum)

print(my_sum[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[3] = "Continuum"
my_tuple.insert(1, "negro")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

#del my_tuple es inmutable, da error