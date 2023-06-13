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


if __name__ == "__main__":
    main()