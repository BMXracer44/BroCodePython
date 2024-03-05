#Alex Ferguson
#3/4/24
#Sets are unordered collections of unique elements which can be used for hashing and more

utensils = {"fork", "spoon", "knife"}
#Only prints knife once
dishes = {"bowl", "plate", "cup", "knife"}
#utensils.update(dishes)
#Prints items in utensils and dishes
#dishes.update(utensils)

#utensils.add("napkin")
#utensils.remove("knife")
#Removes all knifes
#utensils.clear()
#dinner_table = utensils.union(dishes)

#print(dishes.difference(utensils))
print(utensils.intersection(dishes))

#for x in dinner_table:
#    print(x)
#Not necessarily printed in same order as in the set
#Faster than a list if you need to check if something is in the list    
