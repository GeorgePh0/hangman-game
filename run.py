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