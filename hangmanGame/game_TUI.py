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
        # 잘못된 입력에 대한 처리
        if not guessedChar.isalpha():
            UI.errorPrint("""
            =================================
            ==========Input Alphabet=========
            =================================""")
            continue
        if len(guessedChar) is not 1:
            UI.errorPrint("""
            =================================
            =====Input just one character====
            =================================""")
            continue
        if guessedChar in guess.getGuessedList():
            UI.errorPrint("""
            =================================
            =====Input another character=====
            =================================""")
            continue
        # Guess결과에 따른 처리
        result = guess.guess(guessedChar)
        if result is 1:
            break
        if result is 0:
            hangman.minusLife()
        UI.display()
    UI.display()
    UI.endOfGame(hangman.getLife())


if __name__ == "__main__":
    gameMain()