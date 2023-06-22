from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QLabel
from PyQt5 import uic
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi('simplecalc.ui', self)
        self.show()
        self.setWindowTitle('Simple calculator')
        self.btn9.clicked.connect(self.show9)
        self.btn8.clicked.connect(self.show8)
        self.btn7.clicked.connect(self.show7)
        self.btn6.clicked.connect(self.show6)
        self.btn5.clicked.connect(self.show5)
        self.btn4.clicked.connect(self.show4)
        self.btn3.clicked.connect(self.show3)
        self.btn2.clicked.connect(self.show2)
        self.btn1.clicked.connect(self.show1)
        self.btn0.clicked.connect(self.show0)
        self.btnC.clicked.connect(self.clearEf)
        self.btnAdd.clicked.connect(self.Add)
        self.btnEqual.clicked.connect(self.Equal)
        self.show()


    def show9(self):
        text = self.calclabel.text()
        self.calclabel.setText(text+"9")
    def show8(self):
        text = self.calclabel.text()
        self.calclabel.setText(text+"8")
    def show7(self):
        text = self.calclabel.text()
        self.calclabel.setText(text+"7")
    def show6(self):
        text = self.calclabel.text()
        self.calclabel.setText(text+"6")
    def show5(self):
        text = self.calclabel.text()
        self.calclabel.setText(text+"5")
    def show4(self):
        text = self.calclabel.text()
        self.calclabel.setText(text+"4")
    def show3(self):
        text = self.calclabel.text()
        self.calclabel.setText(text+"3")
    def show2(self):
        text = self.calclabel.text()
        self.calclabel.setText(text+"2")
    def show1(self):
        text = self.calclabel.text()
        self.calclabel.setText(text+"1")
    def show0(self):
        text = self.calclabel.text()
        self.calclabel.setText(text+"0")
    def clearEf(self):
        self.calclabel.setText('')

    def Add(self):
        text = self.calclabel.text()
        self.calclabel.setText(text + " + ")

    def Equal(self):
        equation = self.calclabel.text()
        ans = eval(equation)
        self.calclabel.setText(str(ans))

def main():
    app = QApplication([])
    window = Window()
    app.exec_()

if __name__ == '__main__':
    main()