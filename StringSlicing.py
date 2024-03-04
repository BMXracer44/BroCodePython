#Alex Ferguson
#3/3/2024
#Slicing can be used to create substrings by extracting elements from another string 
#Slicing can be helpful when you need to change and extract specific portions of a string
#while keeping the original string intact

#This can be done using indexing[] or slice() functions
#                   [start:stop:step]

name = "Alex Ferguson"

first_name = name[0:4]
#[inclusive:exclusive]

last_name  = name[5:]

funky_name = name[0:len(name):2]
other_name = name[::3]

print(first_name)
print(last_name)
print(funky_name)
print(other_name)

reversed_name = name[::-1]
print(reversed_name)


website = "http://google.com"
website2 = "http://wikipedia.com"
slice = slice(7,-4)

print(website[slice])
print(website2[slice])

#I learned how to grab a substring of a string in Python using the indexing and slice operators
