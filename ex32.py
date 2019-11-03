
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears','apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
    print(f"This is count {number}")
# same as above
for fruit in fruits:
    print(f"A fruit of type:{fruit}")

# also we can go to mixed list too
# notice we have to use {} since we don't know what's in it

for y in change:
    print(f"I got {y}")

# we can also build lists, first start with an empty one
elements = []

# then use the range function  to do 0 to 5 counts
for y in range(0, 6):
    print(f"Adding {y} to the list.")
# append is a function that lists understand
    elements.append(y)

# now we can print them out too
for y in elements:
    print(f"Element was: {y}")
the_count.append('hola')
print(the_count)