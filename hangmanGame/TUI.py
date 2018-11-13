from guess import Guess
from hangman import Hangman

class TextUI:
    def __init__(self, GuessObject, hangmanObject):
        self.GuessObject = GuessObject
        self.hangmanObject = hangmanObject
        self.display()

    def display(self):
        # 결과가 맞는지 틀렸는지 사용자에게 전달
        #print("Correct word: ", self.GuessObject.word)
        print(self.hangmanObject.getPicture())
        shownString = " ".join(self.GuessObject.shownList)
        print("Life: ", self.hangmanObject.getLife())
        print("Word({}): {}".format(self.GuessObject.lengthOfWord, shownString))
        print("Already Tried:", ", ".join(sorted(self.GuessObject.guessedList)))
        print()

    def endOfGame(self, life):
        if life > 0:
            print("""
            =========================================
            =================Success=================
            =========================================
            """, end="")
        else:
            print("""
            =========================================
            ===================Fail==================
            =========================================
            """, end="")
        print("""Answer Word = {}""".format(self.GuessObject.word))
    def errorPrint(self, errorMsg):
        print(errorMsg)
        print()


if __name__ == "__main__":
    c = Guess("abesateda")
    h = Hangman()
    print(c.shownList)
    T = TextUI(c, h)
    c.guess("a")
    T.display()
    if c.guess("z") is False:
        h.minusLife()
    T.display()



