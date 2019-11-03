def add(a, b):
    print(f"adding {a} + {b}")

    return a + b

def subtract(a, b):
    # print(f"subtracting {a} - {b}")
    return a - b

def multiply(a, b):  
    # print(f"multiplying {a} * {b}")
    return a * b

def divide(a,b):
    # print(f"dividing {a} / {b}")
    return a / b

print("lets do some maths with just fuctions!")

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print(f"age : {age}\n height : {height}\n weight : {weight}\n iq : {iq}\n")

# A puzzle for the extra credit, type it in anyway.
print("here is a puzzle.")

# what = add(age, subtract(height, multiply(weight,divide(iq, 2))))
dres = divide(iq, 2)
emres = multiply(weight, dres)
pres = subtract(height, emres)
what = add(age, pres)

print("That becomes: ", what, "can you do it by hand?")