#Alex Ferguson
#3/7/24
#Keyword arguments are arguments preceded by an identifier when we pass them to a fucntion
#The order does not matter

def hello(first,middle,last):
    print("Hello " + first + " " + middle + " " + last)

hello("Bro", "Alex", "Ferguson")    
#Positional arguments - order matters

hello(last = "Ferguson", first = "Bro", middle = "Alex")
#Prints the same thing as above, but arguments are in a different order
