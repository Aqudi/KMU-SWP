import random

class Word:

    def __init__(self, filename):
        f = open(filename, 'r')
        lines = f.readlines()
        f.close()

        self.words = []
        for word in lines:
            self.words.append(word)

    def test(self):
        pass

    def randFromDB(self):
        pass
