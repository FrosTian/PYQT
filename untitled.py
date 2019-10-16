# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(727, 553)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(460, 180, 41, 41))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(40, 190, 168, 24))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(260, 190, 168, 24))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(530, 190, 113, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(230, 190, 21, 20))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "="))
        self.label.setText(_translate("Form", "+"))
        self.pushButton.clicked.connect(lambda: self.add())

    def add(self):
        A = float(self.lineEdit.text())
        B = float(self.lineEdit_2.text())
        self.lineEdit_3.setText(str(A + B))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    Mainwindow = QMainWindow()
    ui = Ui_Form()
    ui.setupUi(Mainwindow)
    Mainwindow.show()
    sys.exit(app.exec_())

