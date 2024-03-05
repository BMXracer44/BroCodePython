#Alex Ferguson
#3/4/2024
#Lists are used to store multiple items in a single variable. 
#Lists are crucial in giving your code options while it is running, without having too many variables

food = ["pizza", "hamburgers", "hot dog", "spaghetti"] 

food[0] = "shushi"

#print(food[0])

#food.append("ice cream")
food.remove("hot dog")
food.pop()
#Removes last item from list
food.insert(0,"cake")
#Inserts item at given position
food.sort()
#Sorts list alphabetically
food.clear()
#Removes all elements

for x in food:
    print(x)
