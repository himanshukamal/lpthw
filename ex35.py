from sys import exit

def gold_room():
    print("This room is full of gold. how much do you take?")

    choice = input("> ")
    # if "0" in choice or "1" in choice:
    if int(choice) < 50:
        how_much = int(choice)
        # else:
        # dead("Man, learn to type a number.")

        # if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("you greedy bastard!")

def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False
    
    # below we create an infinite loop and test the value of choice.
    while True:
        print("""you have 4 options:
            1.take honey
            2.taunt bear and bear not moved
            3.taunt bear and bear moved
            4.open door""")
        choice = input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice =="taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door"and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")

def cthulhu_room():
    print("Here you see the great  evil Cthulhu.")
    print("he, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input("> ")
    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print(why, "Good job!")
    exit(0)

def start():
    print("You are in dark room.")
    print("There is a door to your right and left.")
    print("Which one fo you take?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room untill you starve.")

def signal_handler(signal, frame):
    """This function catches the SIGINT signal from the operating system
    to ensure a graceful shutdown of this script.
    
    i.e. exit gracefully on keyboard interrupt"""
    print("You cant quit!")

def foo():
    pass

# Sometimes we may want to write a .py file that can be both used by other
# programs and/or modules as a module, and can also be run as the main program
# itself. In those cases we can put the code that needs to be run independently
# as main, then we can use the special keyword __name__ and check if its value
# is == "__main__".
if __name__ == "__main__":
    import signal
    try:
        signal.signal(signal.SIGINT, signal_handler)
        start()
    except KeyboardInterrupt:
        pass
    except EOFError:
        pass