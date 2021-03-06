#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QFrame, QApplication)
from PyQt5.QtGui import QColor
from PyQt5 import QtCore


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.col = QColor(0, 0, 0)

        redb = QPushButton('Red', self)
        redb.setCheckable(True)
        redb.move(10, 10)

        redb.clicked[bool].connect(self.setColor)

        greenb = QPushButton('Green', self)
        greenb.setCheckable(True)
        greenb.move(10, 60)

        greenb.clicked[bool].connect(self.setColor)

        blueb = QPushButton('Blue', self)
        blueb.setCheckable(True)
        blueb.move(10, 110)

        blueb.clicked[bool].connect(self.setColor)

        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QtCore.QCoreApplication.quit)
        qbtn.move(170, 600)
        # self.button = qbtn
        # qbtn.show()

        self.square = QFrame(self)
        self.square.setGeometry(150, 20, 500, 500)
        self.square.setStyleSheet("QWidget { background-color: %s }" %
            self.col.name())

        # self.setGeometry(300, 300, 280, 180)
        self.setWindowTitle('Toggle button')
        self.showFullScreen()
        self.show()


    def setColor(self, pressed):

        source = self.sender()

        if pressed:
            val = 255
        else: val = 0

        if source.text() == "Red":
            self.col.setRed(val)
        elif source.text() == "Green":
            self.col.setGreen(val)
        else:
            self.col.setBlue(val)

        self.square.setStyleSheet("QFrame { background-color: %s }" %
            self.col.name())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())