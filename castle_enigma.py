import time
import movements as m

a=2
inventory = []

def intro():
    print("You step through the heavy, creaking doors of the deserted castle...")
    time.sleep(a)
    print("The once grand entrance hall is now a shadowy chamber filled with an eerie silence...")
    time.sleep(a)
    print("In front of you, a long hallway stretches into the depths of the castle, its end lost in darkness...")
    time.sleep(a)
    print("To your right, a stone staircase ascends to a higher level.")
    time.sleep(a)
    print("Press 1: To enter the hallway.")
    print("Press 2: To walk up the stairs.")
    # enter loop 1
    m.loop1()

# ############# MAIN FUNCTION ############# #

castle = '''
                                  |>>>
                                  |
                    |>>>      _  _|_  _         |>>>
                    |        |;| |;| |;|        |
                _  _|_  _    \\.    .  /    _  _|_  _
               |;|_|;|_|;|    \\:. ,  /    |;|_|;|_|;|
               \\..      /    ||;   . |    \\.    .  /
                \\.  ,  /     ||:  .  |     \\:  .  /
                 ||:   |_   _ ||_ . _ | _   _||:   |
                 ||:  .|||_|;|_|;|_|;|_|;|_|;||:.  |
                 ||:   ||.    .     .      . ||:  .|
                 ||: . || .     . .   .  ,   ||:   |
                 ||:   ||:  ,  _______   .   ||: , |
                 ||:   || .   /+++++++\    . ||:   |
                 ||:   ||.    |+++++++| .    ||: . |
              __ ||: . ||: ,  |+++++++|.  . _||_   |
     ____--`~    '--~~__|.    |+++++__|----~    ~`---,              ___
-~--~                   ~---__|,--~'                  ~~----_____-~'   `~----~~
'''
print(castle)
print()
print()
time.sleep(a)
print("You find yourself standing before the imposing gates of a forgotten castle that has long been shrouded in "
      "mystery.")
time.sleep(a)
print("Legends speak of hidden treasures of immeasurable value hidden within its age-old walls.")
time.sleep(a)
print()
startGame = input("Would you like to embark on a quest that promises both fortune and adventure ? (Y/N): ")
if startGame == "n" or startGame == "N":
    print("Maybe next time")
    time.sleep(3)
elif startGame == "y" or startGame == "Y":
    intro()