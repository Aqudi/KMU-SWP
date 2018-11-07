from guess import Guess

class TextUI:
    def __init__(self, GuessObject):
        self.Object = GuessObject
        self.display()
    def display(self):
        # 결과가 맞는지 틀렸는지 사용자에게 전달
        shownString = " ".join(self.Object.shownList)
        print("Word ({}): {}".format(self.Object.lengthOfWord, shownString))

if __name__ == "__main__":
    c = Guess("abesateda")
    print(c.shownList)
    T = TextUI(c)
    c.guess("a")
    T.display()



