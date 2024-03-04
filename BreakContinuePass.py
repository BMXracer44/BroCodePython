#Alex Ferguson
#3/3/24
#Loop control statements which change a loop execution from it's normal sequence

#Break is used to terminate the loop entirely
#Continue skips the next iteration of the loop
#Pass does nothing (Acts like a placeholder)

#while True:
#    name = input("Enter your name: ")
#    if name != "":
#        break

#phone_number = "414-372-5748"

#for i in phone_number:
#    if i == "-":
#        continue
#    print(i, end="")

for i in range(1,21):
    #         (Inclusive, exclusive)
    if i == 13:
        pass
    else:
        print(i)
