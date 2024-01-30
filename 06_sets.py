## set ##

my_set = set()
my_other_set = {}

print(type(my_set))

my_other_set = {"Barbara", "Cordova", 31}

print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("Anais")

print(my_other_set) ## un set no es una estructura ordenada, ni admite repetidos

print("Moure" in my_other_set)
print(31 in my_other_set)

my_other_set.remove("Cordova")
print(my_other_set)

my_other_set.clear()
print(my_other_set)

my_set = {"Barbara", "Cordova", 31}

my_other_set = {"javascript", "ingles", "react"}

my_new_set = my_set.union(my_other_set)
print(my_new_set)

print(my_new_set.difference(my_set))

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

print(len(it_companies))

it_companies.add("Twitter")
print(it_companies)

new_companies = {"Linux", "Continuum", "Globant"}

all_companies = it_companies.union(new_companies)
print(all_companies)


it_companies.discard("Continuum")
print(it_companies)

it_companies.remove('Amazon')
print(it_companies)