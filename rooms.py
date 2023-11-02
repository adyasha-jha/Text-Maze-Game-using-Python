import time
import random
import movements as m


a=2
inventory = []

def hallway():
    print("Strolling down the hallway, you observe... ")
    time.sleep(a)
    print("In the room on the left, a sentinel of steel, cold and unyielding, stands with unwavering resolve.")
    time.sleep(a)
    print("Yet, in its grasp, the soldier's hand remains empty, a silent testament to a sword's absence.")
    time.sleep(a)
    print("On the right, a pantry draped in darkness beckons with the gentle glow of candlelight slipping through its open door.")
    time.sleep(a)
    print("Press 1: To enter the pantry.")
    print("Press 2: To inspect the soldier.")
    # enter loop2

def library():
    print("You enter the library, and the grand room unfolds before you.")
    time.sleep(a)
    print("A large, ornate wooden table sits at the center, strewn with parchments, quills, and inkwells.")
    time.sleep(a)
    any_anagram()
    print("Press 1: To enter the bedchamber.")
    print("Press 2: To enter the armory.")
    m.loop7()

def pantry():
    riddle_parts = {
        "barrels": "IN GLASS, I AGE WITH GRACE, A TREASURE FROM GRAPE'S EMBRACE.",
        "sacks": "RED, WHITE OR BLUSH, I'M THE CONNOISSEUR'S SPACE",
        "jars": "WHAT AM I IN A BOTTLE, TIME'S SWEET EMBRACE."
    }

    print("\n"
          "On entering the pantry you see rows upon rows of meticulously organized\n"
          "supplies from barrels of salted meats and sacks of flour to \n"
          "shelves filled with glass jars containing preserved fruits and vegetables\n")
    time.sleep(a)
    # investigate the barrels
    input("Press Enter to investigate further.")
    print("""While exploring the barrels, your keen eye catches a mysterious inscription etched onto the aged wood.""")
    time.sleep(a)
    print(riddle_parts["barrels"])
    time.sleep(a)
    # investigate the sacks
    print("Then your attention turns to the sacks...")
    time.sleep(a)
    input("Press Enter to keep investigating.")
    time.sleep(a)
    print(riddle_parts["sacks"])
    # Investigate the glass jars
    print("Finally, you investigate the glass jars...")
    time.sleep(a)
    input("Press Enter to reveal the final part of the riddle")
    print(riddle_parts["jars"])
    time.sleep(a)

    # Present the complete riddle
    complete_riddle = f"\nNow that you've uncovered all the clues, can you solve the riddle?\n\n{riddle_parts['barrels']}\n{riddle_parts['sacks']}\n{riddle_parts['jars']}"
    print(complete_riddle)

    while True:
        answer = input("\nEnter your answer: ")
        if answer.lower() == 'wine':
            print("Hmm...'wine'...")
            time.sleep(a)
            print("let's search for the wine barrels...")
            time.sleep(a)
            print("your gaze falls upon one of the wine barrels, \n"
                  "and there, you discover a HIDDEN KEY.")
            break
        else:
            print("That's not the correct answer. Try again.")
    inventory.append('key')


def soldier():
    print("You see on his shield the words printed...")
    time.sleep(a)
    print("'Provide what I seek, and I shall reciprocate in kind.'")
    time.sleep(a)
    print("Let's explore more...")

def upstairs():
    print("Upon the stone steps, your ascent resounds, echoing through the castle's hushed embrace. ")
    time.sleep(a)
    print("Before you, three majestic doors loom, each sheltering untold secrets...")
    print("Press 1: To enter the library.")
    print("Press 2: To enter the bedchamber.")
    print("Press 3: To enter the armory.")

def any_anagram():
    # List of book titles
    book_titles = ["The Great Gatsby", "To Kill a Mockingbird", "Romeo and Juliet", "Pride and Prejudice", "The Catcher in the Rye"]

    # Define anagram function
    def anagram(word):
        letters = list(word)  # Convert word to list of characters
        random.shuffle(letters)  # Shuffle letters randomly
        shuffled_word = ''.join(letters)  # Convert shuffled letters back to string
        return shuffled_word  # Return shuffled word

    # Create dictionary with anagrams
    anagrams = {}
    for title in book_titles:
        anagrams[anagram(title)] = title

    # Choose a random book from the dictionary
    correct_book = random.choice(list(anagrams.values()))

    # Print anagram of correct book
    anagram_of_correct_book = anagram(correct_book)
    print("As you look at the parchments, you see a jumbled sequence of letters...")
    print(anagram_of_correct_book)
    time.sleep(a)
    print("'Umm...Maybe it's an anagram for a book', you think.")
    time.sleep(1)

    while True:
        # Get user input
        guess = input("Which book do you think this anagram represents? ")

        # Check if guess is correct
        if guess.lower() == correct_book.lower():
            print("As you find the correct book name, you go and find the book... ")
            time.sleep(a)
            print("As you open the book, you find an amulet inside it...")
            break  # Exit the loop if the guess is correct
        else:
            print("Sorry, that's not it. Try again.")
    inventory.append('amulet')


def bedchamber():
    print("Using the amulet you found earlier, you step into a bedchamber shrouded in the hushed embrace of time. \n")
    time.sleep(a)
    print("As you investigate the bedchamber, you stumble upon a concealed door. There's a riddle etched onto it:\n")
    print("I'm forged in fire, a weapon of might,\n"
          "In battles, I gleam with a fierce, deadly light.\n"
          "With a hilt and a blade, I'm a warrior's delight,\n"
          "What am I, ready to join the fight?")
    time.sleep(a)
    while True:
        answer = input("\nEnter your answer: ").strip().lower()

        if answer == 'sword':
            print("Hmm...'SWORD'...an abrupt and resounding clamor reverberated through the room, \n"
                  "and just as swiftly, the door swung open, shrouding the chamber in a cloak of uncertainty.")
            input("press ENTER to enter the secret pathway.")
            armory()
            break
        else:
            print("That's not the correct answer. Try again.")


def armory():
    print("You find yourself in a dimly lit armory, a golden sword glinting in the faint light. ")
    time.sleep(a)
    print("The secret door you entered through has now closed behind you, leaving you locked inside.")
    time.sleep(a)
    print(
        "As you pick up the golden sword, it feels powerful in your hand, and you know it's the key to something "
        "greater.")
    time.sleep(a)
    inventory.append('sword')
    print(
        "Your attention shifts to a cryptic cipher, etched on a nearby wall, perhaps the only way to open the armory "
        "door from the inside. ")
    time.sleep(a)
    decipher()
    time.sleep(a)
    print("You walk downstairs ... ")

def decipher():
    correct_msg = 'FREE ME'
    encrypted_msg = 'GSFF NF'
    print(encrypted_msg)
    print("Hint --> apple : bqqmf")
    while True:
        # Get user input
        guess = input("Ans ")

        # Check if guess is correct
        if guess.lower() == correct_msg.lower():
            print("The armory opens... ")
            time.sleep(a)
            print("You are once again facing the stairways...")
            break  # Exit the loop if the guess is correct
        else:
            print("Sorry, that's not it. Try again.")








def guarded_room():
    print("In steel clad silence, a sentinel soldier guards the untold")
    time.sleep(4)
    while True:
        sword = input("enter 'sword' for giving it to the soldier.")
        if sword.lower() == 'sword':
            print("A door ajar, invites you to step into the concealed chamber.")
            time.sleep(2)
            break
        else:
            print("\nPlease give me the sword!")
            print("\n")
    print("""As you enter the chamber, a blinding radiance engulfs your senses, rendering you momentarily sightless.
When you dare to part your eyelids once more, a sight to behold greets you: a TREASURE CHEST.\n""")
    time.sleep(2)
    print("'THIS IS IT!', you think.\n")
    time.sleep(1)
    print("'Oh wait... It seems locked...'")
    if 'key' in inventory:
        have_key()
    else:
        print("You move towards the pantry to find the key...")
        pantry()
        print("With the key in hand, you head back towards the treasure...")


def have_key():
    print("""Summoning the key you discovered in the pantry earlier, 
you carefully insert it into the chest's lock, 
feeling a moment of anticipation as it turns with a gentle click.\n""")
    time.sleep(4)
    print("Congrats, you found the treasure!!")
    print('''
*******************************************************************************
          |                   |                  |                     |
 ________|________________.=""_;=.______________|_____________________|______
|                   |  ,-"_,=""     `"=.|                  |
|__________________|__"=._o`"-.        `"=._____________|__________________
          |                "=._o"=._      `"=.                     |
 ________|_____________________:=._o "=._."_.-="'"=.__________________|______
|                   |    _.--" , ; `"=._o." ,-"""-. ".   |
|__________________|_._"  ,. .` ` `` ,  `"-._"-.   ". '_|__________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;-.o"=._; ." ` '."\ . "-._ /______________|______
|                   | |o;    "-.o"=._``  '` " ,__.--o;   |
|__________________|_| ;     (#) `-.o `"=.`.--"o.-; ;___|__________________
___/______/______/___|o;.    "      `".o|o_.--"    ;o;___/______/______/___
/_____/______/______/_"=._o--.        ; | ;        ; ;/_____/______/______/
___/______/______/______/__"=._o--.   ;o|o;     ._;o;____/______/______/___
/_____/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/
___/______/______/______/______/_____"=.o|o.--""__/______/______/______/___
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************    
''')