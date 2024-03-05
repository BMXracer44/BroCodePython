#Alex Ferguson
#3/4/24
#2D lists are a list of lists which can be used to make a grid or a board in an application


drinks = ["coffee", "soda","tea"]
dinner = ["pizza", "hamburger","hotdog"]
dessert = ["cake", "ice cream"]

food = [drinks, dinner, dessert]

print(food[0][0])
#Displays coffee (specific variable)
print(food[1][2])
print(len(food))
#Prints 3 because 3 lists are in the list. One list is one variable.
