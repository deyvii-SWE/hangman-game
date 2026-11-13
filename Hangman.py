
# imports
from random import choice

# classes
class Interface():
    def __init__(self):
        self.chances_left = 0

    # interfaces
    def display_main_menu(self):
        print("+---------------------------------+")
        print("|          HANGMAN GAME           |")
        print("+---------------------------------+")
        print("|                                 |")
        print("| 1. PLAY                         |")
        print("| 2. EXIT                         |")
        print("|                                 |")
        print("+---------------------------------+")

    def pre_game_menu(self):
        print("+---------------------------------+")
        print("|          HANGMAN GAME           |")
        print("+---------------------------------+")
        print("|                                 |")
        print("| A word in english was randomly  |")
        print("| choose, you have 7 chances to   |")
        print("| guess! Good luck!               |")
        print("|                                 |")
        print("+---------------------------------+")

    def display_hangman(self):
        print("+--------+")
        print("|        |")
        print("|        |")
        print(f"|        {"O" if self.chances_left < 7 else " "}")
        print(f"|       {"/" if self.chances_left < 5 else " "}{"|" if self.chances_left < 6 else " "}{"\\" if self.chances_left < 4 else " "}")
        print(f"|        {"-" if self.chances_left < 3 else " "}")
        print(f"|       {"/" if self.chances_left < 2 else " "} {"\\" if self.chances_left < 1 else " "}")
        print("|")
        print("|")
        print("|")

    def display_chances_left(self):
        print("+-------------------+")
        print(f"|  {self.chances_left} CHANCES LEFT   |")
        print("+-------------------+")

    def display_win_message(self):
        print("+-------------------+")
        print(f"|    You win!!!     |")
        print("+-------------------+")

    def display_lose_message(self):
        print("+-------------------+")
        print(f"|    You lose!!!    |")
        print("+-------------------+")

    # chance logic
    def chance_reduce(self):
        self.chances_left -= 1

    def reset_chances(self):
        self.chances_left = 7

# if the letter of the word are not present in letter_used gonna print a underline, just like a hangman game works 
def print_encrypted_word(word, letter_used):
    for letter in word:
        if letter in letter_used:
            print(f" {str(letter).upper()}", end=" ")
        else:
            print(" _", end=" ")
    print()

# random word list
def get_word():
    word_list = [
        "elephant",
        "mountain",
        "keyboard",
        "sunflower",
        "galaxy",
        "butterfly",
        "thunder",
        "mirror",
        "candle",
        "ocean",
        "pyramid",
        "feather",
        "volcano",
        "diamond",
        "whisper",
        "compass",
        "lantern",
        "telescope",
        "mushroom",
        "waterfall"
    ]

    return choice(word_list)

# just space
def space():
    print("\n"*30)

# instancing interface
interface = Interface()
while True:

    # reset
    interface.reset_chances()
    
    # main menu 
    while True:
        space()
        interface.display_main_menu()
        print()

        # option read
        try:
            option = int(input(" +- Option: "))
            # if the option is less then 1 and more then 2 raise ValueError
            if option < 1 or option > 2:
                raise ValueError

            break
        except ValueError:
            print("+-------------------------------+")
            print("| Please, insert a valid option |")
            print("+-------------------------------+")
            print()
            input("...")

    if option == 2:
        break

    # shows the info how the game works
    space()
    interface.pre_game_menu()
    print()
    input("...")

    # get a random word from word list
    word = get_word()
    letter_used = []
    while interface.chances_left > 0:
        # game info block
        space()
        interface.display_chances_left()
        print()
        interface.display_hangman()
        print_encrypted_word(word, letter_used)
        print()

        # shows letters already used
        print(", ".join(letter.upper() for letter in letter_used))

        # guess part
        try:
            letter_guessed = str(input(" +- Guess: ")).strip().lower()

            # if the letter already was used, repeated or sent more then 1 characteres raise ValueError
            if len(letter_guessed) != 1 or not letter_guessed.isalpha() or letter_guessed in letter_used:
                raise ValueError
                
            letter_used.append(letter_guessed)

            # chance reduce logic
            if letter_guessed not in word:
                interface.chance_reduce()

        except ValueError:
            print("+--------------------------------------------------------------------------+")
            print("| You inserted a number or a repeated letter, please insert a valid letter |")
            print("+--------------------------------------------------------------------------+")
            print()
            input("...")
            continue

        # win/lose conditions
        if all(letter in letter_used for letter in word):
            break
        elif interface.chances_left <= 0:
            break

    # re-show info
    space()
    interface.display_chances_left()
    print()
    interface.display_hangman()
    print_encrypted_word(word, letter_used)
    print()

    # win/lose message display
    if interface.chances_left > 0:
        interface.display_win_message()
        print()
        input("...")
    else:
        interface.display_lose_message()
        print()
        input(f" +- the word was: {word.upper()}")

    


    
