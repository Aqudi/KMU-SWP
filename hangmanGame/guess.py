class Guess:

    def __init__(self, word):
        # 랜덤으로 뽑은 단어를 설정해서 저장해두기
        self.word = word
        self.lengthOfWord = len(self.word)
        self.shownString = "_" * self.lengthOfWord

    def display(self):
        # 결과가 맞는지 틀렸는지 사용자에게 전달
        print("Word {}: {}".format(self.lengthOfWord, self.lengthOfWord))


    def guess(self, character):
        # 사용자로부터 받은 character가 word안에 있는지 없는지 어디에 있는지 판단
        if character in self.word:
            indexList = [character]
            for i in range(self.lengthOfWord):
                if self.shownString[i] == character:
                    indexList.append(i)
            return indexList
        return False