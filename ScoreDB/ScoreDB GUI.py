# 20181708 국민대학교 소프트웨어학과 허태정
# vbox랑 hbox쓰지 말기,
import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt


class Button(QPushButton):

    def __init__(self, text, callback):
        super().__init__()
        self.setText(text)
        self.clicked.connect(callback)


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
        self.lineEdit_name = QLineEdit()
        self.lineEdit_age = QLineEdit()
        self.lineEdit_score = QLineEdit()
        label_name = QLabel("Name", self)
        label_score = QLabel("Score", self)
        label_age = QLabel("Age", self)

        firstLine = QHBoxLayout()
        baseLayout.addLayout(firstLine)
        firstLine.addWidget(label_name)
        firstLine.addWidget(self.lineEdit_name)
        firstLine.addWidget(label_age)
        firstLine.addWidget(self.lineEdit_age)
        firstLine.addWidget(label_score)
        firstLine.addWidget(self.lineEdit_score)

        #두번쨰라인
        self.lineEdit_amount = QLineEdit()
        self.combo = QComboBox()
        self.combo.addItem("Name")
        self.combo.addItem("Age")
        self.combo.addItem("Score")
        label_key = QLabel("Key", self)
        label_amount = QLabel("Amount", self)

        secondLine = QHBoxLayout()
        baseLayout.addLayout(secondLine)
        secondLine.addStretch(1)
        secondLine.addWidget(label_amount)
        secondLine.addWidget(self.lineEdit_amount)
        secondLine.addWidget(label_key)
        secondLine.addWidget(self.combo)

        #세번쨰라인
        self.btn_add = Button("Add", self.buttonClicked)
        self.btn_del = Button("Del", self.buttonClicked)
        self.btn_find = Button("Find", self.buttonClicked)
        self.btn_inc = Button("Inc", self.buttonClicked)
        self.btn_show = Button("Show", self.buttonClicked)

        thirdLine = QHBoxLayout()
        baseLayout.addLayout(thirdLine)
        thirdLine.addStretch(1)
        thirdLine.addWidget(self.btn_add)
        thirdLine.addWidget(self.btn_del)
        thirdLine.addWidget(self.btn_find)
        thirdLine.addWidget(self.btn_inc)
        thirdLine.addWidget(self.btn_show)

        #네 다섯번쨰라인
        label_result = QLabel("Result")
        self.te_result = QTextEdit()
        self.te_result.setReadOnly(True)

        lastLine = QVBoxLayout()
        #vbox.addStretch(1)
        baseLayout.addLayout(lastLine)
        lastLine.addWidget(label_result)
        lastLine.addWidget(self.te_result)
        #vbox.addStretch(1)

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
            print("DB=================================================")
            for index, p in enumerate(sorted(DB, key=lambda person: person[self.combo.currentText()])):
                print("{}.".format(index + 1), end=' ')
                text += (str(index+1)+". ")
                for attr in sorted(p):
                    print(attr + "=" + str(p[attr]), end=' ')
                    text += (attr + "=" + str(p[attr]) + " ")
                text +="\n"
                print()
            self.te_result.setText(text)
            print("===================================================\n")
        else:
            print("정보가 없습니다.\n")


    def buttonClicked(self):
        button = self.sender()
        name = self.lineEdit_name.text()
        age = self.lineEdit_age.text()
        score = self.lineEdit_score.text()
        amount = self.lineEdit_amount.text()
        scoredb = self.scoredb
        key = button.text()
        if key == 'Add':
            print("add")
            try:
                age = int(age)
                score = int(score)
                record = {'Name': name, 'Age': age, 'Score': score}
                scoredb += [record]
                self.showScoreDB(scoredb)
            except ValueError:
                print("Age, Score에 숫자를 넣어주세요.\n")
                pass

        elif key == 'Del':
            print("Del")
            for p in scoredb[:]:
                if p['Name'] == name:
                    scoredb.remove(p)
            self.showScoreDB(scoredb)

        elif key == 'Show':
            print("Show")
            self.showScoreDB(scoredb)

        elif key == 'Find':
            print("Find")
            temp = []
            for p in scoredb:
                if p['Name'] == name:
                    temp += [p]
            self.showScoreDB(temp)
        elif key == 'Inc':
            print("Inc")
            try:
                amount = int(amount)
                for p in scoredb:
                    if p['Name'] == name:
                        p['Score'] += amount
            except ValueError:
                print("Amount에 숫자를 입력해주세요.\n")
                pass
            self.showScoreDB(scoredb)

        self.lineEdit_name.setText("")
        self.lineEdit_age.setText("")
        self.lineEdit_score.setText("")
        self.lineEdit_amount.setText("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())
