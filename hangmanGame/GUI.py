from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLayout, QGridLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton

from guess import Guess
from hangman import Hangman


class TextEdit(QTextEdit):
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
        self.guessButton.setText(name)
        self.guessButton.clicked.connect(callback)


class GraphicUI(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.guess = Guess
        self.hangman = Hangman

        # Hangman display window
        self.hangmanWindow = TextEdit()

        # Layout
        hangmanLayout = QGridLayout()
        hangmanLayout.addWidget(self.hangmanWindow, 0, 0)

        # Main Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addLayout(hangmanLayout, 0, 0)

        self.setLayout(mainLayout)

        self.setWindowTitle('Hangman Game')



if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    game = GraphicUI()
    game.show()
    sys.exit(app.exec_())