#Alex Ferguson
#3/4/24
#Tuples are like lists but cannot be changed once created. This is helpful for 
#immutability and ordered collections

student = ("Alex", 21, "male")

print(student.count("Alex"))
print(student.index("male"))

for x in student:
    print(x)

if "Alex" in student:
    print("Alex is here")    