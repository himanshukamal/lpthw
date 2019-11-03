# assigning values to variables
people = 50
cars = 40 
trucks = 15

#print the boolean expression if the condition is true
if cars > people or trucks < cars:
    print(cars > people or trucks < cars)
else:
    print("try again")
if cars > people:
    print("We should take the cars.")

elif cars < people:
    print("We should not take the cars.")
else: 
    print("We cant decide.")


if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, lets stay home then.")