# takes a word from the words file
from words import word_list
# selects a random word
import random
# clears terminal
import os


def clear_console():
    """
    Function to clear terminal
    """
    os.system('clear')


# Selects the word at random
def grab_word():
    """
    Function to pick a random word from the list in the saved data
    """
    word = random.choice(word_list)
    return word.upper()


# Gives the player a welcome message and asks for their name
def welcome():
    """
    Function that prints the opening message,
    and also asks player to input their name
    """
    print("Welcome to hangman. \n\n"
          "You have 6 guesses to complete the word. \n\n"
          "All words are from football teams in England. \n\n")
    player = " "
    while True:
        player = input("Please enter your name: ")
        if player.isalpha() is not True:
            print("Error: Please enter letters only.")
            continue
        else:
            print("\n")
            print(f'Hi {player}, welcome and also GOOD LUCK.')
            return player


def replay():
    """
    Function to replay the game
    """
    restart = input("would you like to play again! Enter Y or N \n")
    if restart == "y":
        clear_console()
        main()
    else:
        print("Thanks for playing!")


# Start the game
def start_game(word):
    """
    Function to start the game
    """
    # Define variables
    word_answer = "_ " * len(word)
    letter_guessed = []
    guessed = False
    tries = 6
    print(display_hangman(tries))  # prints the hangman images
    print(word_answer)
    # player hasn't discovered the word and still has tries left to guess
    while guessed is False and tries > 0:
        guess = input("Select a letter: ").upper()
        # Can only try one letter at a time
        if len(guess) == 1 and guess.isalpha():
            if guess in letter_guessed:
                print("%s has already been used." % guess)
            elif guess not in word:
                print("%s is not in the word." % guess)
                letter_guessed.append(guess)
                tries -= 1
                print(display_hangman(tries))
            elif guess in word:
                print("Good Job!", guess, "is in the word")
                letter_guessed.append(guess)
                print(display_hangman(tries))
            else:
                print("Invalid. Please choose a letter.")
        else:
            print("Not a valid guess. Please choose a letter.")
    # print the letter if it is in the word
        current = ""
        if guessed is False:
            for letter in word:
                if letter in letter_guessed:
                    current += letter
                else:
                    current += "_ "
            print(current)
    # word is completed
        if current == word:
            guessed = True
            print("Well Done!!!")
            replay()
        elif tries == 0:
            print(display_hangman(tries))
            print(word)
            print("")
            print("Oh No! Better luck next time")


# Displays different images, every time the player picks the wrong letter
def display_hangman(tries):
    """
    Function that visually shows each incorrect try
    the player makes in the game
    """
    stages = ["""
               +---+
               o   |
              /|\  |
              / \  |
                  ===""",
              """
               +---+
               o   |
              /|\  |
              /    |
                  ===""",
              """
               +---+
               o   |
              /|\  |
                   |
                  ===""",
              """
               +---+
               o   |
              /|   |
                   |
                  ===""",
              """
               +---+
               o   |
               |   |
                   |
                  ===""",
              """
               +---+
               o   |
                   |
                   |
                  ===""",
              """
               +---+
                   |
                   |
                   |
                  ==="""]
    return stages[tries]


# Loads the terminal and starts the gmae
def main():
    """
    Main Function to play the game
    """
    word = grab_word()
    welcome()
    start_game(word)


if __name__ == "__main__":
    main()
