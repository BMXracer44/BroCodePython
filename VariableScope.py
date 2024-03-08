#Alex Ferguson
#3/7/24
#Scope is the region that a variable is recognized

name = "Alex" #Global scope (available inside and outside the function)
#Possible to have a global and local version of the same variable
#LEGB order for python

def display_name():
    #name = "Ferguson" #Local scope (Available only inside function)
    print(name)

display_name()
print(name)
#Will not work because variable is not in global scope    