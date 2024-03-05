#Alex Ferguson
#3/4/24
#Indexing can be used to manipulate elements in variables (str, list, tuples)

name = "alex Ferguson!"

#if(name[0].islower()):
#    name = name.capitalize()

first_name = name[: name.find(' ')].upper()
last_name = name[name.find(' ') + 1:].lower()
last_character = name[-1]

print(first_name)
print(last_name)
print(last_character)

