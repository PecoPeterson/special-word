# special-word
This script is a game that attempts to guess a word chosen by the user. The user inputs a number between 1 and 12, which represents the length of the word they have chosen. The script then reads a file called "words.txt" which contains a list of words, and filters the words to only include those that match the length provided by the user.

The script then narrows down the list of possible words by asking the user if certain letters are in the word, and if so, in which positions. The script continues to filter the list of words based on the user's input until it is able to guess the correct word.

The script also keeps track of the number of times it has guessed incorrectly, and prints this at the end of the game.

The script is made of several functions, each one responsible for a specific task:
