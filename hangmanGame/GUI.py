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

    def __init__(self, parent=None):
        super().__init__(parent)
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
        self.guessButton.setEnabled(False)

        # new game Button
        self.newGameButton = ToolButton('New Game', self.newGameClicked)
        self.newGameButton.setEnabled(True)

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

    def display(self):
        self.hangmanWindow.setPlaceholderText(self.hangmanObject.getPicture())
        self.currentWord.setText(self.GuessObject.getShownString())
        self.guessedChars.setText(" ".join(self.GuessObject.getGuessedList()))

    def guessClicked(self):
        guessedChar = self.charInput.text()
        self.charInput.clear()
        self.message.clear()
        self.newGameButton.setEnabled(True)

        if len(guessedChar) != 1:
            return self.message.setText("Input just one chracter")
        if not guessedChar.isalpha:
            return self.message.setText("Input Alphabet")
        if guessedChar in self.GuessObject.getGuessedList():
            return self.message.setText("Input another chracter")

        result = self.GuessObject.guess(guessedChar)

        if result is 1:
            self.guessButton.setEnabled(False)
            self.message.setText("Success")
        if result is 0:
            self.hangmanObject.minusLife()

        self.display()
        if self.hangmanObject.getLife() <= 0:
            self.guessButton.setEnabled(False)
            self.newGameButton.setEnabled(True)
            return self.message.setText("Game Over '{}'".format(self.GuessObject.getWord('word')))

    def newGameClicked(self):
        from word import Word
        word = Word('words.txt')
        self.GuessObject = Guess(word.randFromDB())
        self.hangmanObject = Hangman()

        self.guessButton.setEnabled(True)
        self.newGameButton.setEnabled(False)

        self.charInput.clear()
        self.message.clear()
        self.currentWord.clear()
        self.display()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    game = GraphicUI()
    game.show()
    sys.exit(app.exec_())