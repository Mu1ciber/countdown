import sys
from random import randint

from PyQt5 import QtCore, QtWidgets


class Ui(QtWidgets):
    unused_letter_num = 1
    VOKALE = ["A", "E", "I", "O", "U"]

    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self, ):
        self.konsonant = QtWidgets.QPushButton(self.centralwidget)
        self.konsonant.setObjectName("konsonant")
        self.vokal = QtWidgets.QPushButton(self.centralwidget)
        self.vokal.setObjectName("vokal")
        self.vokal.clicked.connect(self.vokal_generator)
        self.beenden = QtWidgets.QPushButton(self.centralwidget)
        self.beenden.setObjectName("beenden")
        self.beenden.clicked.connect(QtCore.QCoreApplication.instance().quit)

    def vokal_generator(self):
        new_vokal = Ui.VOKALE[randint(0, 4)]

        self.letter.setText(str(new_vokal))

        print("Vokal pressed")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui()
    sys.exit(app.exec_())
