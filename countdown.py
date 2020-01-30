from random import randint
import sys
from PyQt5 import QtWidgets, uic, QtCore


class Ui(QtWidgets.QMainWindow):
    VOKALE = ["A", "E", "I", "O", "U"]
    unused_text_labels = 1

    def __init__(self):
        super(Ui, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('countdown.ui', self)  # Load the .ui file
        self.initUI()

    def initUI(self):
        self.resize(300, 200)

        self.vokal = self.findChild(QtWidgets.QPushButton, "vokal")  # Find Vokal Button
        self.vokal.clicked.connect(self.vokal_generator)

        self.konsonant = self.findChild(QtWidgets.QPushButton, "konsonant")  # Find Konsonant Button

        self.exit = self.findChild(QtWidgets.QPushButton, "beenden")  # Find beenden Button
        self.exit.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.labels = []
        for i in range(1, 10):
            name = "buchstabe_{}".format(i)
            label = self.findChild(QtWidgets.QLabel, name)
            self.labels.append(label)

        self.show()  # Show the GUI1

    def vokal_generator(self):
        new_vokal = Ui.VOKALE[randint(0, 4)]
        self.labels[Ui.unused_text_labels].setText(new_vokal)
        Ui.unused_text_labels += 1
        print("Vokal pressed")


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
