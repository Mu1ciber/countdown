import sys
from random import randint

from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    unused_letter_num = 1
    VOKALE = ["A", "E", "I", "O", "U"]

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(810, 641)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.konsonant = QtWidgets.QPushButton(self.centralwidget)
        self.konsonant.setGeometry(QtCore.QRect(574, 200, 81, 23))
        self.konsonant.setObjectName("konsonant")
        self.vokal = QtWidgets.QPushButton(self.centralwidget)
        self.vokal.setGeometry(QtCore.QRect(110, 200, 75, 23))
        self.vokal.setObjectName("vokal")
        self.vokal.clicked.connect(self.vokal_generator)
        self.beenden = QtWidgets.QPushButton(self.centralwidget)
        self.beenden.setGeometry(QtCore.QRect(690, 560, 75, 23))
        self.beenden.setObjectName("beenden")
        self.beenden.clicked.connect(QtCore.QCoreApplication.instance().quit)

        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 300, 689, 73))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.buchstabe_1 = QtWidgets.QTextEdit(self.layoutWidget)
        self.buchstabe_1.setObjectName("buchstabe_1")
        self.gridLayout.addWidget(self.buchstabe_1, 0, 0, 1, 1)
        self.buchstabe_2 = QtWidgets.QTextEdit(self.layoutWidget)
        self.buchstabe_2.setObjectName("buchstabe_2")
        self.gridLayout.addWidget(self.buchstabe_2, 0, 1, 1, 1)
        self.buchstabe_3 = QtWidgets.QTextEdit(self.layoutWidget)
        self.buchstabe_3.setObjectName("buchstabe_3")
        self.gridLayout.addWidget(self.buchstabe_3, 0, 2, 1, 1)
        self.buchstabe_4 = QtWidgets.QTextEdit(self.layoutWidget)
        self.buchstabe_4.setObjectName("buchstabe_4")
        self.gridLayout.addWidget(self.buchstabe_4, 0, 3, 1, 1)
        self.buchstabe_5 = QtWidgets.QTextEdit(self.layoutWidget)
        self.buchstabe_5.setObjectName("buchstabe_5")
        self.gridLayout.addWidget(self.buchstabe_5, 0, 4, 1, 1)
        self.buchstabe_6 = QtWidgets.QTextEdit(self.layoutWidget)
        self.buchstabe_6.setObjectName("buchstabe_6")
        self.gridLayout.addWidget(self.buchstabe_6, 0, 5, 1, 1)
        self.buchstabe_7 = QtWidgets.QTextEdit(self.layoutWidget)
        self.buchstabe_7.setObjectName("buchstabe_7")
        self.gridLayout.addWidget(self.buchstabe_7, 0, 6, 1, 1)
        self.buchstabe_8 = QtWidgets.QTextEdit(self.layoutWidget)
        self.buchstabe_8.setObjectName("buchstabe_8")
        self.gridLayout.addWidget(self.buchstabe_8, 0, 7, 1, 1)
        self.buchstabe_9 = QtWidgets.QTextEdit(self.layoutWidget)
        self.buchstabe_9.setObjectName("buchstabe_9")
        self.gridLayout.addWidget(self.buchstabe_9, 0, 8, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 810, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.buchstabe_1.append("blub")
        letter = "buchstabe_{}".format(Ui_MainWindow.unused_letter_num)
        for i in range(1, 10):
            label = getattr(, "buchstabe_{}".format(i))
            label.setText("Blub")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.konsonant.setText(_translate("MainWindow", "Konsonant"))
        self.vokal.setText(_translate("MainWindow", "Vokal"))
        self.beenden.setText(_translate("MainWindow", "Beenden"))

    def vokal_generator(self):
        new_vokal = Ui_MainWindow.VOKALE[randint(0, 4)]

        self.letter.setText(str(new_vokal))

        print("Vokal pressed")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
