import random

class Word:

    def __init__(self, filename):
        f = open(filename, 'r')
        lines = f.readlines()
        f.close()

        self.words = []
        for word in lines:
            word = word.rstrip()
            self.words.append(word)
        print('%d words in DB' % len(self.words))


    def test(self):
        for word in self.words:
            print(word)


    def randFromDB(self):
        r = random.randrange(len(self.words))
        return self.words[r]
