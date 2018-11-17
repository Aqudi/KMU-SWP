from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLayout, QGridLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton

from guess import Guess
from hangman import Hangman


class LineEdit(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setReadOnly(True)
        self.setAlignment(Qt.AlignCenter)
        font = self.font()
        font.setFamily('Courier New')
        self.setFont(font)


class ToolButton(QToolButton):
    def __init__(self, name, callback):
        super().__init__()
        self.setText(name)
        self.clicked.connect(callback)


class GraphicUI(QWidget):

    def __init__(self, GuessObject, hangmanObject, parent=None):
        super().__init__(parent)

        # Objects for getting impormation
        self.GuessObject = GuessObject
        self.hangmanObject = hangmanObject
        self.result = 2 # default status 2 means incorrect but not fail

        # Hangman display window
        self.hangmanWindow = QTextEdit()
        self.hangmanWindow.setReadOnly(True)
        self.hangmanWindow.setAlignment(Qt.AlignLeft)
        font = self.hangmanWindow.font()
        font.setFamily('Courier New')
        self.hangmanWindow.setFont(font)

        # Hangman Layout
        hangmanLayout = QGridLayout()
        hangmanLayout.addWidget(self.hangmanWindow, 0, 0)

        # Widget displaying current status
        self.currentWord = LineEdit()
        font.setPointSize(font.pointSize() + 8)
        self.currentWord.setFont(font)

        # Widget displaying already used chracters
        self.guessedChars = LineEdit()
        self.guessedChars.setMaxLength(52)

        # Widget displaying message output
        self.message = LineEdit()
        self.message.setMaxLength(52)

        # Widget user inputting character
        self.charInput = LineEdit()
        self.charInput.setMaxLength(1)
        self.charInput.setReadOnly(False)

        # Guess Button
        self.guessButton = ToolButton('Guess!', self.guessClicked)

        # new game Button
        self.newGameButton = ToolButton('New Game', self.newGameClicked)

        # Status Layout
        statusLayout = QGridLayout()
        statusLayout.addWidget(self.currentWord, 0, 0, 1, 2)
        statusLayout.addWidget(self.guessedChars, 1, 0, 1, 2)
        statusLayout.addWidget(self.message, 2, 0, 1, 2)
        statusLayout.addWidget(self.charInput, 3, 0)
        statusLayout.addWidget(self.guessButton, 3, 1)
        statusLayout.addWidget(self.newGameButton, 4, 0)

        # Main Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addLayout(hangmanLayout, 0, 0)
        mainLayout.addLayout(statusLayout, 0, 1)

        self.setLayout(mainLayout)

        self.setWindowTitle('Hangman Game')

        self.display()

    def display(self):
        self.hangmanWindow.setPlaceholderText(self.hangmanObject.getPicture())
        self.setCurrentWord(self.GuessObject.getShownString())
        self.setGuessedChars(self.GuessObject.getGuessedString())

    def setCurrentWord(self, string):
        self.currentWord.setText(string)

    def setGuessedChars(self, string):
        self.guessedChars.setText(string)

    def setMessage(self, string):
        self.message.setText(string)

    def guessClicked(self):
        self.result = self.GuessObject.guess(self.charInput.text())
        self.charInput.clear()
        self.display()

    def getResult(self):
        return self.result

    def newGameClicked(self):
        pass


if __name__ == '__main__':
    from guess import Guess
    from hangman import Hangman
    import sys

    app = QApplication(sys.argv)
    g = Guess("abcdefg")
    h = Hangman()
    game = GraphicUI(g, h)
    game.show()
    sys.exit(app.exec_())