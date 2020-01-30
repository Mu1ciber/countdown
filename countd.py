import sys

from PyQt5.QtWidgets import *
from PyQt5 import QtCore


class Fenster(QWidget):
    def __init__(self):
        super().__init__()
        self.initMe()

    def initMe(self):
        self.setWindowTitle("Countdown-Game")
        self.button = QPushButton("Press me!!!", self)
        self.button.move(100, 100)
        self.button.clicked.connect(self.pressed)
        self.text = QTextBrowser(self)
        self.text.setGeometry(0, 0, 50, 50)
        self.text.setText("test")
        self.text2 = QTextBrowser(self)
        self.text2.setGeometry(50, 50, 100, 100)
        self.text2.setText("test2")
        self.show()

    def pressed(self):
        i = 30
        print("Ich wurde gedrückt!!!")
        self.text.setText(str(i))


app = QApplication(sys.argv)
w = Fenster()
sys.exit(app.exec_())
