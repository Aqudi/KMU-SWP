class Guess:

    def __init__(self, word):
        # 랜덤으로 뽑은 단어를 설정해서 저장해두기
        self.word = word
        self.lengthOfWord = len(self.word)
        self.shownList = []
        self.guessedList = []
        for i in range(self.lengthOfWord):
            self.shownList.append("_")

    def guess(self, character):
        # 사용자로부터 받은 character가 word안에 있는지 없는지 어디에 있는지 판단
        self.guessedList.append(character)

        if character in self.word:
            for i in range(self.lengthOfWord):
                if self.word[i] == character:
                    self.shownList[i] = character
            shownString = "".join(self.shownList)
            if shownString == self.word:
                return True
            else:
                return shownString
        return False

if __name__ == "__main__":
    c = Guess("abcdaeaf")
    print(c.shownList)
    print(c.guess("a"))
    d = Guess("abc")
    d.guess("a")
    d.guess("b")
    print(d.guess("c"))
