#Alex Ferguson
#3/7/24
#Arguments are parameters that will pack all arguments into a tuple
#Useful so a function can accept a varying amount of arguments

def add(*args):
    sum = 0
    args = list(args)
    args[0] = 0
    for i in args:
        sum += i
    return sum    

print(add(1, 2, 3, 4, 5, 6))
