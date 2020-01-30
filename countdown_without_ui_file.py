import sys
from random import randint
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QGridLayout, QApplication, QGroupBox


class Ui(QWidget):
    unused_labels = 0

    def __init__(self):
        super().__init__()
        self.initUi()
        self.setWindowTitle("Countdown-Game")

    def initUi(self):

        self.vokal = QPushButton("Vokal", self)
        self.vokal.move(200, 100)
        self.vokal.clicked.connect(self.vokal_generator)

        self.labels = []
        for i in range(1, 10):
            label = QLabel(self)
            label.setObjectName("buchstabe_{}".format(i))
            label.setText("a")
            self.labels.append(label)
        self.createGridLayout()
        self.show()

    def createGridLayout(self):
        layout = QGridLayout()
        for i in range(9):
            layout.addWidget(self.labels[i], 0, i)
        Ui.setLayout(self, layout)

    def vokal_generator(self):
        VOKALE = ["A", "E", "I", "O", "U"]

        new_vokal = VOKALE[randint(0, 4)]
        self.labels[Ui.unused_labels].setText(new_vokal)
        print("Vokal pressed")
        Ui.unused_labels += 1


app = QApplication(sys.argv)
window = Ui()
sys.exit(app.exec_())
