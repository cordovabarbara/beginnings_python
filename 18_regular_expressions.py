# Regular Expressions #

import re

my_string = "Esta es la leccion de expresiones regulares, esta es la Leccion del dia"

my_other_string = "Esta no es la leccion de expresiones regulares"


match = re.match("Esta es la leccion", my_string, re.I)
print(match)

print(re.match("Esta es la leccion", my_other_string))

start, end = match.span()
print(my_string[start:end])

# search

search = re.search("Leccion", my_string, re.I)
print(search)
start, end = search.span()
print(my_string[start: end])

# findall

findall = re.findall("leccion", my_string, re.I)
print(findall)

# Split
print(re.split(":", my_string))

# sub
print(re.sub("expresiones regulares", "RegEx", my_string))
print(re.sub("[l|L]eccion", "LECCION", my_string))