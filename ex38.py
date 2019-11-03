ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("wait there are not 10 things in the list. Let's fix that.")

# seperate items of string by a space
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Songs", "Frisbee", "Corn", "Banana", "Girl","Boys"]

while len(stuff) != 10:
    next_one = more_stuff.pop() #poping items from last and storing them in next_one
    print("Adding: ", next_one) #showing what is to be print and going to added 
    stuff.append(next_one)#appending items from more_stuff to stuff
    print(f"There are {len(stuff)} items now.")# printing the length of  list stuff 

print("There we go: ", stuff)# printing the list

print("Lets do some things with stuff.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))
