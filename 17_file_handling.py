## File Handling ##

txt_file = open("./my_file.txt", "r+")
#print(txt_file.read())
#print(txt_file.read(10))
#print(txt_file.readline())
#print(txt_file.readlines())

for line in txt_file.readlines():
    print(line)
print(txt_file.readline())
txt_file.close()

# json file

import json

json_file = open("./my_file.json", "w+")

my_json = {
    "Nombre":"Anais",
    "Apellido":"Cordova", 
    "Edad":31, 
    "Lenguajes":"Python",
    "Profesion":"informatico"
}

json.dump(my_json, json_file, indent = 2)

