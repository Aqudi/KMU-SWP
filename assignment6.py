import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt

class ScoreDB(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB(self.scoredb)

    def initUI(self):
        #베이스 레이아웃
        baseLayout = QVBoxLayout()

        # 첫번째라인
        lb_name = QLabel("Name", self)
        le_name = QLineEdit()
        lb_age = QLabel("Age", self)
        le_age = QLineEdit()
        lb_score = QLabel("Score", self)
        le_score = QLineEdit()

        hbox = QHBoxLayout()
        baseLayout.addLayout(hbox)
        hbox.addWidget(lb_name)
        hbox.addWidget(le_name)
        hbox.addWidget(lb_age)
        hbox.addWidget(le_age)
        hbox.addWidget(lb_score)
        hbox.addWidget(le_score)

        #두번쨰라인
        lb_amount = QLabel("Amount", self)
        le_amount = QLineEdit()
        lb_key = QLabel("Key", self)
        self.combo = QComboBox()
        self.combo.addItem("Name")
        self.combo.addItem("Age")
        self.combo.addItem("Score")

        hbox2 = QHBoxLayout()
        baseLayout.addLayout(hbox2)
        hbox2.addStretch(1)
        hbox2.addWidget(lb_amount)
        hbox2.addWidget(le_amount)
        hbox2.addWidget(lb_key)
        hbox2.addWidget(self.combo)

        #세번쨰라인
        btn_add = Button("Add", self.buttonClicked)
        btn_del = Button("Del", self.buttonClicked)
        btn_find = Button("Find", self.buttonClicked)
        btn_inc = Button("Inc", self.buttonClicked)
        btn_show = Button("Show", self.buttonClicked)

        hbox3 = QHBoxLayout()
        baseLayout.addLayout(hbox3)
        hbox3.addStretch(1)
        hbox3.addWidget(btn_add)
        hbox3.addWidget(btn_del)
        hbox3.addWidget(btn_find)
        hbox3.addWidget(btn_inc)
        hbox3.addWidget(btn_show)

        #네 다섯번쨰라인
        lb_result = QLabel("Result")
        self.te_result = QTextEdit()
        self.te_result.setReadOnly(True)

        vbox = QVBoxLayout()
        baseLayout.addLayout(vbox)
        vbox.addStretch(1)
        vbox.addWidget(lb_result)
        vbox.addWidget(self.te_result)

        self.setLayout(baseLayout)
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        self.show()

    def closeEvent(self, event):
        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb = pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()


    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self, DB):
        if DB:
            text = ""
            for index, p in enumerate(sorted(DB, key=lambda person: person[self.combo.currentText()])):
                print("{}.".format(index + 1), end=' ')
                text += (str(index+1)+". ")
                for attr in sorted(p):
                    print(attr + "=" + str(p[attr]), end=' ')
                    text += (attr + "=" + str(p[attr]) + " ")
                text +="\n"
            self.te_result.setText(text)
        else:
            print("정보가 없습니다.")

    class Button(QPushButton):

        def __init__(self, text, callback):
            super().__init__()
            self.setText(text)
            self.clicked.connect(callback)

    def buttonClicked(self):
        button = self.sender()
        key = button.text()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())
