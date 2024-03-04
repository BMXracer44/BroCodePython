#Alex Ferguson 
#3/3/24
#If statements are used to complete high level programs and for decision making in coing
#Since I have already learned about if statements in a previous class, I am only glossing over this one

age = int(input("How old are you?: "))

if age == 100:
    print("You are a century old!")
elif age >= 18:
    print("You are an adult!")
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You are a child!")
    
            