from guess import Guess

class TUI:
    def __init__(self):
        self.display()
        self.shownString = ""

    def display(self, guessedList):
        # 결과가 맞는지 틀렸는지 사용자에게 전달
        for index in guessedList[1:]:
            del Guess.shownList[index]
            Guess.shownList.insert(index, guessedList[0])
        self.shownString.join("")
        print("Word ({}): {}".format(Guess.lengthOfWord, self.shownString))

if __name__ == "__main__":
    word = "abest"
    T = TUI


