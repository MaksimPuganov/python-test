#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QFrame, QApplication, QMessageBox)
from PyQt5.QtGui import QColor
from PyQt5 import QtCore


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        # qbtn = QPushButton('Quit', self)
        # qbtn.clicked.connect(QtCore.QCoreApplication.quit)
        # qbtn.move(170, 600)
        # self.button = qbtn
        # qbtn.show()

        mb = QMessageBox()
        mb.setIcon(QMessageBox.Information)
        mb.setWindowTitle('Error')
        mb.setText('Array not loaded, make sure you take picture or import an image first.')
        mb.showFullScreen()
        mb.exec()

        # self.setGeometry(300, 300, 280, 180)
        self.setWindowTitle('Toggle button')
        self.showFullScreen()
        self.show()



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())