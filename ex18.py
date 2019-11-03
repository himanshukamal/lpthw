# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just take one argument
def print_one(arg1):
    print(f"arg1 : {arg1}")

#this on takes no arguments
def print_none():
    print("I got nothin'.")

def print_mini(firstname, lastname, *args):
    print(f"my name is {firstname} {lastname}")
    for sport in args:
        print(f"i like {sport}")
    
#print_two("Zed", "Shaw")
#print_two_again("Zed","shaw")
#print_one("First!")

#print_none()
print_mini("himanshu", "kamal", "football", "running", "pool")