# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\JaniL\Documents\GitHub\hirviporukka_fork\hirviporukka\manualDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(270, 304)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 231, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 10, 252, 284))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelLogo = QtWidgets.QLabel(self.widget)
        self.labelLogo.setMinimumSize(QtCore.QSize(250, 250))
        self.labelLogo.setMaximumSize(QtCore.QSize(250, 250))
        self.labelLogo.setText("")
        self.labelLogo.setPixmap(QtGui.QPixmap("c:\\Users\\JaniL\\Documents\\GitHub\\hirviporukka_fork\\hirviporukka\\docs/Pictures/logo.png"))
        self.labelLogo.setScaledContents(True)
        self.labelLogo.setObjectName("labelLogo")
        self.verticalLayout.addWidget(self.labelLogo)
        self.closePushButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.closePushButton.setFont(font)
        self.closePushButton.setObjectName("closePushButton")
        self.verticalLayout.addWidget(self.closePushButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Käyttöohje"))
        self.label.setText(_translate("Dialog", "Placeholder käyttöohjeikkuna"))
        self.closePushButton.setText(_translate("Dialog", "Sulje"))
