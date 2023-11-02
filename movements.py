import rooms as r
import time
a=2

def loop1():
    player_choice = action()

    if player_choice == '1':
         r.hallway()
         loop2()

    elif player_choice == '2':
        r.upstairs()
        loop3()
        first_staircase_then_hallway()

def loop2():
    player_choice = action()

    if player_choice == "1":
        r.pantry()
        loop6()

    elif player_choice == "2":
            r.soldier()
            print("Press 1: To enter the pantry.")
            print("Press 2: To move up the stairs.")
            next_choice = action()
            if next_choice == "1":
                r.pantry()
                loop6()
            elif next_choice == "2":
                r.upstairs()
                loop3()
                soldier_upstairs()


def loop6():
    print("Press 1: To inspect the soldier.\nPress 2: To go upstairs. ")
    next_choice = action()
    if next_choice == "1":
        r.soldier()
        print("As you find nothing more downstairs, you decide to move up the stairs...")
        time.sleep(a)
        r.upstairs()
        loop3()
        pantry_upstairs()

    elif next_choice == "2":
        r.upstairs()
        loop3()
        pantry_upstairs()

def pantry_upstairs():

    print("As you walk the Hallway again, you recall that you already got a key from the pantry...")
    time.sleep(a)
    input("Press ENTER To head towards the room guarded by the soldier.")
    r.guarded_room()


def soldier_upstairs():
    print("You walk the Hallway...")
    print("Press 1: To enter the pantry.")
    print("Press 2: To inspect the soldier.")
    choice = action()
    if choice == "1":
        r.pantry()
        time.sleep(a)
        print("Now let's head to the final room...")
        r.guarded_room()
    elif choice == "2":
        r.guarded_room()


def loop3():
    player_choice = action1()

    if player_choice == "1":
        r.library()
    elif player_choice == "2":
        print("You approach the door of the bedchamber, but upon inspection,you notice that it's locked.")
        print("Press 1: To enter the library.")
        print("Press 2: To enter the armory.")
        loop4()
    elif player_choice == "3":
        print("You approach the door of the armory, but upon inspection, you notice that it's locked from the inside.")
        time.sleep(a)
        print("A message is scrawled on the door, 'The armory can only be opened from the inside.'")
        print("Press 1: To enter the library.")
        print("Press 2: To enter the bedchamber.")
        loop5()


def loop4():
    user_input = action()

    if user_input == "1":
        r.library()
    elif user_input == "2":
        print("You approach the door of the armory, but upon inspection, you notice that it's locked from the inside.")
        time.sleep(a)
        print("A message is scrawled on the door, 'The armory can only be opened from the inside.'")
        print("Press 1: To enter the library.")
        print("Press 2: To enter the bedchamber.")
        loop5()


def loop5():
    user_input = action()

    if user_input == "1":
        r.library()
    elif user_input == "2":
        print("You approach the door of the bedchamber, but upon inspection,you notice that it's locked.")
        print("Press 1: To enter the library.")
        print("Press 2: To enter the armory.")
        loop4()


def loop7():

    user_input = action()

    if user_input == "1":
        r.bedchamber()
    elif user_input == "2":
        print("You approach the door of the armory, but upon inspection, you notice that it's locked from the inside.")
        time.sleep(a)
        print("A message is scrawled on the door, 'The armory can only be opened from the inside.'")
        print("You have already explored the library, it's time to enter the bedchamber...")
        time.sleep(4)
        r.bedchamber()

def first_staircase_then_hallway():
    print("Press 1: To enter pantry.")
    print("Press 2: To head towards the guarding soldier.")

    user_choice = action()
    r.hallway()
    if user_choice == "1":
        r.pantry()
        time.sleep(a)
        print("Now let's head to the final room...")
        r.guarded_room()

    elif user_choice == "2":
        r.guarded_room()

def action():
    choice = ""
    options = ['1', '2']
    while choice not in options:
        choice = input("> ")

        if choice not in options:
            print("Invalid choice")

    return choice

def action1():
    choice = ""
    options = ['1', '2','3']
    while choice not in options:
        choice = input("> ")

        if choice not in options:
            print("Invalid choice")

    return choice