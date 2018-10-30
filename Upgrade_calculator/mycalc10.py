from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout

from keypad import numPadList, operatorList, constantList
from constant import constantMap, romanLetters
from functions import functionList, functionMap

class Button(QToolButton):

    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size

class LineEdit(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setReadOnly(True)
        self.setAlignment(Qt.AlignRight)
        self.setMaxLength(30)


class Calculator(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Display Window
        displayLayout = QGridLayout()
        self.displayResult = LineEdit()
        self.displayCurrentInput = LineEdit()

        displayLayout.addWidget(self.displayCurrentInput, 0, 0, 1, 0)
        displayLayout.addWidget(self.displayResult, 1, 0, 2, 0)

        # Button Creation and Placement
        numLayout = QGridLayout()
        opLayout = QGridLayout()
        constLayout = QGridLayout()
        funcLayout = QGridLayout()

        buttonGroups = {
            'num': {'buttons': numPadList, 'layout': numLayout, 'columns': 3},
            'op': {'buttons': operatorList, 'layout': opLayout, 'columns': 2},
            'constants': {'buttons': constantList, 'layout': constLayout, 'columns': 1},
            'functions': {'buttons': functionList, 'layout': funcLayout, 'columns': 1},
        }

        for label in buttonGroups.keys():
            r = 0; c = 0
            buttonPad = buttonGroups[label]
            for btnText in buttonPad['buttons']:
                button = Button(btnText, self.buttonClicked)
                buttonPad['layout'].addWidget(button, r, c)
                c += 1
                if c >= buttonPad['columns']:
                    c = 0; r += 1

        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mainLayout.addLayout(displayLayout, 0, 0, 1, 0)
        mainLayout.addLayout(numLayout, 1, 0)
        mainLayout.addLayout(opLayout, 1, 1)
        mainLayout.addLayout(constLayout, 2, 0)
        mainLayout.addLayout(funcLayout, 2, 1)

        self.setLayout(mainLayout)

        self.setWindowTitle("My Calculator")


    def buttonClicked(self):
        display = self.displayResult
        currentInput = self.displayCurrentInput
        button = self.sender()
        key = button.text()

        if "Error!" in currentInput.text():
            currentInput.setText(currentInput.text()[:len(currentInput.text())-len("Error!")])
        elif "Error" in currentInput.text():
            self.clearDisplays()
        if key == '=':
            if display.text().find("Error") is -1:
                result = self.evalWithExcept(currentInput.text())
                currentInput.setText(str(result))
        elif key == 'back':
            currentInput.setText(currentInput.text()[:len(currentInput.text())-1])
        elif key == 'C':
            self.clearDisplays()

        elif key == '(':
            try:
                idx = len(currentInput.text())-1
                chr = currentInput.text()[idx]
                if chr.isdigit() or chr == ")":
                    currentInput.setText(currentInput.text() + "*(")
                else:
                    currentInput.setText(currentInput.text() + "(")
            except IndexError:
                currentInput.setText(currentInput.text() + "(")

        elif key in constantList:
            currentInput.setText(display.text() + constantMap[key])

        elif key in functionList:
            """complimentString = ""
            n = "default"
            for i in range(len(currentInput.text())-1, -1, -1):
                if len(currentInput.text()) == 1:
                    n = currentInput.text()[i]
                    break
                elif currentInput.text().isdigit():
                    n=currentInput.text()
                    break
                elif currentInput.text()[i] not in numPadList and currentInput.text()[i] not in romanLetters:
                    n = currentInput.text()[i+1:]
                    complimentString = currentInput.text()[:i+1]
                    break
            if n == "default":
                n = currentInput.text()
            value = functionMap[functionList.index(key)][1](n)
            currentInput.setText(complimentString + value)"""
            result = self.evalWithExcept(currentInput.text())
            currentInput.setText(functionMap[functionList.index(key)][1](result))
        else:
            currentInput.setText(currentInput.text() + key)

        if key not in operatorList[:5] and key:
            if currentInput.text():
                result = self.evalWithExcept(currentInput.text())
                display.setText(result)
            else:
                display.setText("")

    def evalWithExcept(self, string):
        try:
            result = eval(str(string))
            return str(result)
        except ZeroDivisionError:
            return 'Error:0으로 나눌 수 없습니다.'
        except SyntaxError:
            return 'Error:잘못된 수식입니다!'
        except NameError:
            return string

    def clearDisplays(self):
        self.displayResult.clear()
        self.displayCurrentInput.clear()



if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())


""" 
        if "Error" in currentInput.text():
             self.clearDisplays()
        elif display.text() and key in operatorList[:4]:
             if status.text() == key and currentInput.text():
                 key = "="
        elif display.text() and status.text() is "":
             self.clearDisplays()
             
        elif key in operatorList[:4]:
            if display.text() and currentInput.text() is "":
                status.setText(key)
        else:
                display.setText(currentInput.text())
                status.setText(key)
                currentInput.clear()

"""