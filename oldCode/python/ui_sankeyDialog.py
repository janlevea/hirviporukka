# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/jani/GitHub-repos/RasekoSyksy22/hirviporukka/oldCode/python/sankeyDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_sankeyDialog(object):
    def setupUi(self, sankeyDialog):
        sankeyDialog.setObjectName("sankeyDialog")
        sankeyDialog.resize(627, 609)
        self.sankeyWebEngineView = QtWebEngineWidgets.QWebEngineView(sankeyDialog)
        self.sankeyWebEngineView.setGeometry(QtCore.QRect(10, 10, 611, 581))
        self.sankeyWebEngineView.setStyleSheet("")
        self.sankeyWebEngineView.setUrl(QtCore.QUrl("file:///home/jani/GitHub-repos/RasekoSyksy22/hirviporukka/meatstreams.html"))
        self.sankeyWebEngineView.setObjectName("sankeyWebEngineView")

        self.retranslateUi(sankeyDialog)
        QtCore.QMetaObject.connectSlotsByName(sankeyDialog)

    def retranslateUi(self, sankeyDialog):
        _translate = QtCore.QCoreApplication.translate
        sankeyDialog.setWindowTitle(_translate("sankeyDialog", "Sankey-kaavio"))
from PyQt5 import QtWebEngineWidgets
