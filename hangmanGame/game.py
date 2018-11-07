from hangman import Hangman
from guess import Guess
from word import Word
from TUI import TextUI

def gameMain():
    word = Word('words.txt')
    guess = Guess(word.randFromDB())
    hangman = Hangman()
    UI = TextUI(guess, hangman)

    while hangman.getLife() > 0:
        guessedChar = input("Select a letter: ")
        if guess.guess(guessedChar) is False:
            hangman.minusLife()
        UI.display()

if __name__ == "__main__":
    gameMain()