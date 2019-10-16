# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'led.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
import led_rc

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(788, 643)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(100, 180, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.graphicsView = QtWidgets.QGraphicsView(Form)
        self.graphicsView.setGeometry(QtCore.QRect(310, 140, 201, 191))
        self.graphicsView.setStyleSheet("background-image: url(:/led/圆形 (1).png);\n"
"background-image: url(:/led/圆形 (2).png);")
        self.graphicsView.setObjectName("graphicsView")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    Mainwindow = QMainWindow()
    ui = Ui_Form()
    ui.setupUi(Mainwindow)
    Mainwindow.show()
    sys.exit(app.exec_())