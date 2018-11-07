from hangman import Hangman
from guess import Guess
from word import Word
from TUI import TextUI

def gameMain():
    word = Word('words.txt')
    guess = Guess(word.randFromDB())
    hangman = Hangman()
    UI = TextUI(guess, hangman)

    isFinished = False

    while hangman.getLife() > 0:
        guessedChar = input("Select a letter: ")
        isFinished = guess.guess(guessedChar)

        if len(guessedChar) is not 1:
            UI.errorPrint("Input just one character")
        elif isFinished is False:
            hangman.minusLife()

        UI.display()
        if isFinished == True:
            break
    UI.endOfGame(isFinished)


if __name__ == "__main__":
    gameMain()