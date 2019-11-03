from sys import exit

def monster1():
    print("you have 3 weapons now.\n"
        "There is a pistol, 2 grenades and 1 sniper.\n"
        "the monster is on the edge of a cliff of a mountain\n"
        " and gets killed when he falls down on the molten  lava\n"
        "where and with which weapon do you hit him?\n"
        "1. Grenade on head\n"
        "2. Two pistol bullets on legs\n"
        "3. One sniper shot below knee.\n"
    ) 
    while True:
        choice = input()
        if choice == "1":
            dead("monster sees you and kill you")
        elif choice == "2":
            print("congratulations you can move forward")
            monster2()
        elif choice == "3":
            print("congratulations you can move forward.")
            monster2()
        else:
            print("what are you smoking these days?\n"
                "I dont know what do you want to do.\n"
                "select option 1, 2 or 3"
            )

def monster2():
    print("here you see a monster called boogyman.\n"
        "you have 3 weapons. pistol, grenade and sniper.\n"
        "only headshot will kill him\n"
    )
    choice = input("> ")
    if choice == "pistol":
        print("you get to live")
    elif choice == "grenade":
        dead("you are killed")
    elif choice == "sniper":
        print("you get to live")
    else:
        monster2()
    exit(1)

def dead(msg):
    print(msg,"bye bye!")
    exit(0)

def start_room():
    name = input("What is you name: ")
    money = input("how much money do you want: ")

    if int(money) >= 10:
        print("Death is chasing you\n"
            "you are running for your life and you have 2 doors to escape.\n"
            "which one will you take door1 or door2?\n"
        )

        choice = input("> ")
        if choice == "door1":
            print("monster1 world")
            monster1()
        else:
            print("monster 2 world")
            monster2()


start_room()            
    