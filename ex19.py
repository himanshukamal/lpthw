# cheese_and_cracker function that takes in 2 parameters cheese_count and 
# boxes_of_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

# calling the function and passing  20 and 30 as parameter .
print("We can just give the function numbers directly:")
cheese_and_crackers(20,30)

# define two variables to hold amount of cheese and crackers
print("OR,we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

# call the function again which now takes in new varibles.
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# we can also use mathematical operations while pasing the function parameters.  
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# we can also combine variables and math operation.
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# cheesefactory takes in  3 variable value i.e location ,labour_count, revenue.
def cheesefactory(location, labour_count, revenue):
    print(f"\nthe location of cheese factory is {location}")
    print(f"the count of labour force is {labour_count}")
    print(f"the revenue of cheese factory is {revenue}\n")

# call function and passing chandigarh, 100, $3 million as parameters.
print("giving the values directly")
cheesefactory("chandigarh", 100, "$3 million")

print("OR, use variables from the script")
location = "chandigarh"
lab_count = 100
total_revenue = "$3 million"

cheesefactory(location, lab_count, total_revenue)

print("we can also do concatination operation")
cheesefactory( "chandigarh" + "ludhiana", 50 + 50, "$3" + "million")

print("combination of varible and math operation")
cheesefactory(location + "14", lab_count + 15, total_revenue + "and $40,000 ")

# take input from the user
location = input("enter the location: ")
lab_count = input("enter the labour count: ")
total_revenue = input("enter the  Annual total revenue: ")

cheesefactory(location, lab_count, total_revenue)