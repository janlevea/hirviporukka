# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\JaniL\Documents\GitHub\hirviporukka_fork\hirviporukka\groupInfoMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(382, 483)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.meatSharedTableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.meatSharedTableWidget.setGeometry(QtCore.QRect(20, 40, 341, 171))
        self.meatSharedTableWidget.setRowCount(4)
        self.meatSharedTableWidget.setColumnCount(3)
        self.meatSharedTableWidget.setObjectName("meatSharedTableWidget")
        self.groupSummaryTableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.groupSummaryTableWidget.setGeometry(QtCore.QRect(20, 260, 341, 171))
        self.groupSummaryTableWidget.setRowCount(4)
        self.groupSummaryTableWidget.setColumnCount(3)
        self.groupSummaryTableWidget.setObjectName("groupSummaryTableWidget")
        self.meatSharedLabel = QtWidgets.QLabel(self.centralwidget)
        self.meatSharedLabel.setGeometry(QtCore.QRect(30, 10, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.meatSharedLabel.setFont(font)
        self.meatSharedLabel.setObjectName("meatSharedLabel")
        self.groupSummaryLabel = QtWidgets.QLabel(self.centralwidget)
        self.groupSummaryLabel.setGeometry(QtCore.QRect(30, 230, 331, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupSummaryLabel.setFont(font)
        self.groupSummaryLabel.setObjectName("groupSummaryLabel")
        self.refreshPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.refreshPushButton.setGeometry(QtCore.QRect(210, 10, 151, 23))
        self.refreshPushButton.setObjectName("refreshPushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 382, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.meatSharedLabel.setText(_translate("MainWindow", "Jaetut lihat"))
        self.groupSummaryLabel.setText(_translate("MainWindow", "Jakoryhmien yhteenveto"))
        self.refreshPushButton.setText(_translate("MainWindow", "Päivitä"))
