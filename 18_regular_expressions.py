# Regular Expressions #

import re

my_string = "Esta es la leccion de expresiones regulares"

my_other_string = "Esta no es la leccion de expresiones regulares"


match = re.match("Esta es la leccion", my_string, re.I)
print(match)

print(re.match("Esta es la leccion", my_other_string))

start, end = match.span()
print(my_string[start:end])

# search

search = re.search("leccion", my_string, re.I)
print(search)
start, end = search.span()
print(my_string[start: end])