#Alex Ferguson 
#3/3/24
#Logical operators are crucial for most high level programs
#Since I have already learned about logical operators in another class, I am only glossing over this one

temp = int(input("What is the temperature outside?: "))

if temp >= 60 and temp <= 80:
    print("The temperature is good today!")
    print("Go outside!")
elif temp < 60 or temp > 80:
    print("The  temperature is bad today!")
    print("Stay inside!")    