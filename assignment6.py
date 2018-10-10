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
        self.showScoreDB()

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
            self.scoredb =  pickle.load(fH)
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

    def showScoreDB(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())
