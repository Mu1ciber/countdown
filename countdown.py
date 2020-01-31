from random import randint
import sys
from PyQt5 import QtWidgets, uic, QtCore


class Ui(QtWidgets.QMainWindow):
    VOKALE = ["A", "E", "I", "O", "U"]
    KONSONANTEN = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y",
                   "Z"]
    unused_text_labels = 0

    def __init__(self):
        super(Ui, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('countdown.ui', self)  # Load the .ui file
        self.setWindowTitle("Countdown-Game")
        self.initUI()
        
    def initUI(self):
        self.vokal = self.findChild(QtWidgets.QPushButton, "vokal")  # Find Vokal Button
        self.vokal.clicked.connect(self.vokal_generator)  # call function

        self.konsonant = self.findChild(QtWidgets.QPushButton, "konsonant")  # Find Konsonant Button
        self.konsonant.clicked.connect(self.konsonanten_generator)  # call function

        self.exit = self.findChild(QtWidgets.QPushButton, "exit")  # Find beenden Button
        self.exit.clicked.connect(QtCore.QCoreApplication.instance().quit)  # quit

        self.again = self.findChild(QtWidgets.QPushButton, "again")
        self.again.clicked.connect(self.restart)

        self.error_msg = self.findChild(QtWidgets.QLabel, "error_msg")

        self.labels = []
        for i in range(1, 10):  # find all labels
            name = "buchstabe_{}".format(i)
            label = self.findChild(QtWidgets.QLabel, name)
            self.labels.append(label)
        self.show()  # Show the GUI1

    def vokal_generator(self):
        if Ui.unused_text_labels < 9:
            new_vokal = Ui.VOKALE[randint(0, 4)]
            self.labels[Ui.unused_text_labels].setText(new_vokal)
            Ui.unused_text_labels += 1
        else:
            self.error_msg.setText("Du hast schon 9 Buchstaben!")
        print("Vokal pressed")

    def konsonanten_generator(self):
        if Ui.unused_text_labels < 9:
            new_konsonant = Ui.KONSONANTEN[randint(0, 21)]
            self.labels[Ui.unused_text_labels].setText(new_konsonant)
            Ui.unused_text_labels += 1
        else:
            self.error_msg.setText("Du hast schon 9 Buchstaben!")
        print("Konsonant pressed")

    def restart(self):
        for i in self.labels:
            i.setText("")
        self.error_msg.setText("")
        Ui.unused_text_labels = 0
        print("restart pressed")

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
