#Alex Ferguson
#3/3/24
#Nested loops can be important if you want to build high level programs efficently
#Since I have worked with nested loops in other languages, I am only glossing over this
#video to be familiar with the language

rows = int(input("How many rows are there?: "))
col = int(input("How many columns are there?: "))
symbol = input("What symbol do you want to use? ")
#Ex. $, @, #

for i in range(rows):
    for j in range(col):
        print(symbol, end="")
        #Prevents cursor moving to next line
    print()    


