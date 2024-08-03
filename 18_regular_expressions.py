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

#Patterns

pattern = r"[lL]eccion"
print(re.findall(pattern, my_string))


pattern = r"[lL]eccion|expresiones"
print(re.findall(pattern, my_string))

pattern = r"[a-z]"
print(re.findall(pattern, my_string))

pattern = r"[0-9]"
print(re.findall(pattern, my_string))

pattern = r"[a-z]"
print(re.findall(pattern, my_string))

pattern = r"\d"
print(re.findall(pattern, my_string))

pattern = r"[l]."
print(re.findall(pattern, my_string))

pattern = r"[l].*"
print(re.findall(pattern, my_string))

# email validation regular expression 
email = "barbara123@att.com"
pattern = r"^[a-zA-Z0-9]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9]+$"
print(re.match(pattern, email))
print(re.findall(pattern, email))

#exercise
'''Clean the following text. After cleaning, count three most frequent words in the string.
print(most_frequent_words(cleaned_text)) # [(3, 'I'), (2, 'teaching'), (2, 'teacher')]'''

sentence = "%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?"

clean_text = re.sub(r'[^a-zA-Z\s]', '',sentence)
print(clean_text)







