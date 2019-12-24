import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


def window():
    app = QApplication(sys.argv)
    win = QWidget()
    button1 = QPushButton(win)
    button1.setText("Show dialog!")
    button1.move(50, 40)
    button1.clicked.connect(showDialog)
    button2 = QPushButton(win)
    button2.setText("Show dialog!")
    button2.move(50, 90)
    button2.clicked.connect(showDialog)
    win.setWindowTitle("Стартовое окно")
    win.show()
    sys.exit(app.exec_())


def showDialog():
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText("Message box pop up window")
    msgBox.setWindowTitle("QMessageBox")
    msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    msgBox.buttonClicked.connect(msgButtonClick)

    returnValue = msgBox.exec()
    if returnValue == QMessageBox.Ok:
        print('OK clicked')


def msgButtonClick(i):
    print("Button clicked is:", i.text())


if __name__ == '__main__':
    window()