# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/jani/GitHub-repos/RasekoSyksy22/hirviporukka/QT_UI_files/aboutDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(289, 481)
        self.labelLogo = QtWidgets.QLabel(Dialog)
        self.labelLogo.setGeometry(QtCore.QRect(20, 10, 250, 250))
        self.labelLogo.setMinimumSize(QtCore.QSize(250, 250))
        self.labelLogo.setMaximumSize(QtCore.QSize(250, 250))
        self.labelLogo.setText("")
        self.labelLogo.setPixmap(QtGui.QPixmap("/home/jani/GitHub-repos/RasekoSyksy22/hirviporukka/QT_UI_files/../docs/Pictures/logo_ilman_tekstia_Square310x310Logo.scale-150.png"))
        self.labelLogo.setScaledContents(True)
        self.labelLogo.setObjectName("labelLogo")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(20, 270, 250, 161))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 231, 141))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelVersion = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelVersion.setFont(font)
        self.labelVersion.setStyleSheet("color: rgb(0, 0, 0);")
        self.labelVersion.setAlignment(QtCore.Qt.AlignCenter)
        self.labelVersion.setObjectName("labelVersion")
        self.verticalLayout.addWidget(self.labelVersion)
        self.labelBy = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelBy.setFont(font)
        self.labelBy.setStyleSheet("color: rgb(0, 0, 0);")
        self.labelBy.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBy.setObjectName("labelBy")
        self.verticalLayout.addWidget(self.labelBy)
        self.labelBy2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelBy2.setFont(font)
        self.labelBy2.setStyleSheet("color: rgb(0, 0, 0);")
        self.labelBy2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBy2.setObjectName("labelBy2")
        self.verticalLayout.addWidget(self.labelBy2)
        self.labelBy.raise_()
        self.labelVersion.raise_()
        self.labelBy2.raise_()
        self.closePushButton = QtWidgets.QPushButton(Dialog)
        self.closePushButton.setGeometry(QtCore.QRect(20, 440, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.closePushButton.setFont(font)
        self.closePushButton.setObjectName("closePushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Tietoa ohjelmasta"))
        self.labelVersion.setText(_translate("Dialog", "Versio: 1.0"))
        self.labelBy.setText(_translate("Dialog", "2022 Raseko"))
        self.labelBy2.setText(_translate("Dialog", "TiVi-koodarit"))
        self.closePushButton.setText(_translate("Dialog", "Sulje"))
import resources_rc
