from guess import Guess
from hangman import Hangman

class TextUI:
    def __init__(self, GuessObject, hangmanObject):
        self.GuessObject = GuessObject
        self.hangmanObject = hangmanObject
        self.display()
    def display(self):
        # 결과가 맞는지 틀렸는지 사용자에게 전달
        print("Word: ", self.GuessObject.word)
        print("Life: ", self.hangmanObject.getLife())
        print(self.hangmanObject.getPicture())
        shownString = " ".join(self.GuessObject.shownList)
        print("Word ({}): {}".format(self.GuessObject.lengthOfWord, shownString))

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


