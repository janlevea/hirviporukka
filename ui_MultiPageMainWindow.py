# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\JaniL\Documents\GitHub\hirviporukka_fork\hirviporukka\MultiPageMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(804, 608)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 781, 551))
        self.tabWidget.setLocale(QtCore.QLocale(QtCore.QLocale.Finnish, QtCore.QLocale.Finland))
        self.tabWidget.setObjectName("tabWidget")
        self.summaryPage = QtWidgets.QWidget()
        self.summaryPage.setObjectName("summaryPage")
        self.layoutWidget = QtWidgets.QWidget(self.summaryPage)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 531, 501))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sharedMeatLabel = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.sharedMeatLabel.setFont(font)
        self.sharedMeatLabel.setObjectName("sharedMeatLabel")
        self.horizontalLayout.addWidget(self.sharedMeatLabel)
        self.summaryRefreshPushButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.summaryRefreshPushButton.setFont(font)
        self.summaryRefreshPushButton.setObjectName("summaryRefreshPushButton")
        self.horizontalLayout.addWidget(self.summaryRefreshPushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.meatSharedTableWidget = QtWidgets.QTableWidget(self.layoutWidget)
        self.meatSharedTableWidget.setStyleSheet("")
        self.meatSharedTableWidget.setObjectName("meatSharedTableWidget")
        self.meatSharedTableWidget.setColumnCount(0)
        self.meatSharedTableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.meatSharedTableWidget)
        spacerItem = QtWidgets.QSpacerItem(40, 25, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.groupSummaryLabel = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupSummaryLabel.setFont(font)
        self.groupSummaryLabel.setObjectName("groupSummaryLabel")
        self.verticalLayout.addWidget(self.groupSummaryLabel)
        self.groupSummaryTableWidget = QtWidgets.QTableWidget(self.layoutWidget)
        self.groupSummaryTableWidget.setObjectName("groupSummaryTableWidget")
        self.groupSummaryTableWidget.setColumnCount(0)
        self.groupSummaryTableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.groupSummaryTableWidget)
        self.summarySuggestGroupBox = QtWidgets.QGroupBox(self.summaryPage)
        self.summarySuggestGroupBox.setGeometry(QtCore.QRect(559, 9, 201, 501))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.summarySuggestGroupBox.setFont(font)
        self.summarySuggestGroupBox.setObjectName("summarySuggestGroupBox")
        self.tabWidget.addTab(self.summaryPage, "")
        self.killPage = QtWidgets.QWidget()
        self.killPage.setObjectName("killPage")
        self.saveShotPushButton = QtWidgets.QPushButton(self.killPage)
        self.saveShotPushButton.setGeometry(QtCore.QRect(690, 250, 81, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.saveShotPushButton.setFont(font)
        self.saveShotPushButton.setObjectName("saveShotPushButton")
        self.layoutWidget1 = QtWidgets.QWidget(self.killPage)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 110, 759, 51))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.animalLabel = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.animalLabel.setFont(font)
        self.animalLabel.setObjectName("animalLabel")
        self.horizontalLayout_4.addWidget(self.animalLabel)
        self.ageGroupLabel = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ageGroupLabel.setFont(font)
        self.ageGroupLabel.setObjectName("ageGroupLabel")
        self.horizontalLayout_4.addWidget(self.ageGroupLabel)
        self.genderLabel = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.genderLabel.setFont(font)
        self.genderLabel.setObjectName("genderLabel")
        self.horizontalLayout_4.addWidget(self.genderLabel)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.animalComboBox = QtWidgets.QComboBox(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.animalComboBox.setFont(font)
        self.animalComboBox.setObjectName("animalComboBox")
        self.horizontalLayout_5.addWidget(self.animalComboBox)
        self.ageGroupComboBox = QtWidgets.QComboBox(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.ageGroupComboBox.setFont(font)
        self.ageGroupComboBox.setObjectName("ageGroupComboBox")
        self.horizontalLayout_5.addWidget(self.ageGroupComboBox)
        self.genderComboBox = QtWidgets.QComboBox(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.genderComboBox.setFont(font)
        self.genderComboBox.setObjectName("genderComboBox")
        self.horizontalLayout_5.addWidget(self.genderComboBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.killsKillsTableWidget = QtWidgets.QTableWidget(self.killPage)
        self.killsKillsTableWidget.setGeometry(QtCore.QRect(10, 370, 751, 151))
        self.killsKillsTableWidget.setObjectName("killsKillsTableWidget")
        self.killsKillsTableWidget.setColumnCount(0)
        self.killsKillsTableWidget.setRowCount(0)
        self.label = QtWidgets.QLabel(self.killPage)
        self.label.setGeometry(QtCore.QRect(10, 350, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.layoutWidget2 = QtWidgets.QWidget(self.killPage)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 5, 761, 101))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.shotByLabel = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.shotByLabel.setFont(font)
        self.shotByLabel.setObjectName("shotByLabel")
        self.gridLayout_2.addWidget(self.shotByLabel, 0, 0, 1, 1)
        self.shotDateLabel = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.shotDateLabel.setFont(font)
        self.shotDateLabel.setObjectName("shotDateLabel")
        self.gridLayout_2.addWidget(self.shotDateLabel, 0, 1, 1, 1)
        self.shotByComboBox = QtWidgets.QComboBox(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.shotByComboBox.setFont(font)
        self.shotByComboBox.setObjectName("shotByComboBox")
        self.gridLayout_2.addWidget(self.shotByComboBox, 1, 0, 1, 1)
        self.shotDateEdit = QtWidgets.QDateEdit(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.shotDateEdit.setFont(font)
        self.shotDateEdit.setLocale(QtCore.QLocale(QtCore.QLocale.Finnish, QtCore.QLocale.Finland))
        self.shotDateEdit.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.shotDateEdit.setCalendarPopup(True)
        self.shotDateEdit.setDate(QtCore.QDate(2022, 11, 15))
        self.shotDateEdit.setObjectName("shotDateEdit")
        self.gridLayout_2.addWidget(self.shotDateEdit, 1, 1, 1, 1)
        self.verticalLayout_8.addLayout(self.gridLayout_2)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.locationLabel = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.locationLabel.setFont(font)
        self.locationLabel.setObjectName("locationLabel")
        self.verticalLayout_7.addWidget(self.locationLabel)
        self.locationLineEdit = QtWidgets.QLineEdit(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.locationLineEdit.setFont(font)
        self.locationLineEdit.setObjectName("locationLineEdit")
        self.verticalLayout_7.addWidget(self.locationLineEdit)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        self.layoutWidget3 = QtWidgets.QWidget(self.killPage)
        self.layoutWidget3.setGeometry(QtCore.QRect(10, 250, 671, 97))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.additionalInfoLabel = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.additionalInfoLabel.setFont(font)
        self.additionalInfoLabel.setObjectName("additionalInfoLabel")
        self.verticalLayout_9.addWidget(self.additionalInfoLabel)
        self.additionalInfoTextEdit = QtWidgets.QPlainTextEdit(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.additionalInfoTextEdit.setFont(font)
        self.additionalInfoTextEdit.setObjectName("additionalInfoTextEdit")
        self.verticalLayout_9.addWidget(self.additionalInfoTextEdit)
        self.layoutWidget4 = QtWidgets.QWidget(self.killPage)
        self.layoutWidget4.setGeometry(QtCore.QRect(380, 170, 381, 46))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.usageLabel = QtWidgets.QLabel(self.layoutWidget4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.usageLabel.setFont(font)
        self.usageLabel.setObjectName("usageLabel")
        self.verticalLayout_21.addWidget(self.usageLabel)
        self.usageComboBox = QtWidgets.QComboBox(self.layoutWidget4)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.usageComboBox.setFont(font)
        self.usageComboBox.setObjectName("usageComboBox")
        self.verticalLayout_21.addWidget(self.usageComboBox)
        self.layoutWidget5 = QtWidgets.QWidget(self.killPage)
        self.layoutWidget5.setGeometry(QtCore.QRect(10, 170, 361, 46))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.layoutWidget5)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.weightLabel = QtWidgets.QLabel(self.layoutWidget5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.weightLabel.setFont(font)
        self.weightLabel.setObjectName("weightLabel")
        self.verticalLayout_11.addWidget(self.weightLabel)
        self.weightLineEdit = QtWidgets.QLineEdit(self.layoutWidget5)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.weightLineEdit.setFont(font)
        self.weightLineEdit.setObjectName("weightLineEdit")
        self.verticalLayout_11.addWidget(self.weightLineEdit)
        self.tabWidget.addTab(self.killPage, "")
        self.sharePage = QtWidgets.QWidget()
        self.sharePage.setObjectName("sharePage")
        self.shareSavePushButton = QtWidgets.QPushButton(self.sharePage)
        self.shareSavePushButton.setGeometry(QtCore.QRect(680, 232, 81, 41))
        self.shareSavePushButton.setObjectName("shareSavePushButton")
        self.shareSuggestGroupBox = QtWidgets.QGroupBox(self.sharePage)
        self.shareSuggestGroupBox.setGeometry(QtCore.QRect(10, 290, 751, 221))
        self.shareSuggestGroupBox.setObjectName("shareSuggestGroupBox")
        self.layoutWidget6 = QtWidgets.QWidget(self.sharePage)
        self.layoutWidget6.setGeometry(QtCore.QRect(10, 10, 751, 213))
        self.layoutWidget6.setObjectName("layoutWidget6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget6)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.shareKillsLabel = QtWidgets.QLabel(self.layoutWidget6)
        self.shareKillsLabel.setObjectName("shareKillsLabel")
        self.verticalLayout_2.addWidget(self.shareKillsLabel)
        self.shareKillsTableWidget = QtWidgets.QTableWidget(self.layoutWidget6)
        self.shareKillsTableWidget.setObjectName("shareKillsTableWidget")
        self.shareKillsTableWidget.setColumnCount(0)
        self.shareKillsTableWidget.setRowCount(0)
        self.verticalLayout_2.addWidget(self.shareKillsTableWidget)
        self.layoutWidget7 = QtWidgets.QWidget(self.sharePage)
        self.layoutWidget7.setGeometry(QtCore.QRect(10, 230, 101, 41))
        self.layoutWidget7.setObjectName("layoutWidget7")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.layoutWidget7)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget7)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_17.addWidget(self.label_2)
        self.shareDateEdit = QtWidgets.QDateEdit(self.layoutWidget7)
        self.shareDateEdit.setLocale(QtCore.QLocale(QtCore.QLocale.Finnish, QtCore.QLocale.Finland))
        self.shareDateEdit.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.shareDateEdit.setCalendarPopup(True)
        self.shareDateEdit.setDate(QtCore.QDate(2022, 11, 15))
        self.shareDateEdit.setObjectName("shareDateEdit")
        self.verticalLayout_17.addWidget(self.shareDateEdit)
        self.layoutWidget8 = QtWidgets.QWidget(self.sharePage)
        self.layoutWidget8.setGeometry(QtCore.QRect(120, 230, 171, 41))
        self.layoutWidget8.setObjectName("layoutWidget8")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.layoutWidget8)
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget8)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_18.addWidget(self.label_3)
        self.portionComboBox = QtWidgets.QComboBox(self.layoutWidget8)
        self.portionComboBox.setObjectName("portionComboBox")
        self.verticalLayout_18.addWidget(self.portionComboBox)
        self.layoutWidget9 = QtWidgets.QWidget(self.sharePage)
        self.layoutWidget9.setGeometry(QtCore.QRect(300, 230, 161, 41))
        self.layoutWidget9.setObjectName("layoutWidget9")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.layoutWidget9)
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget9)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_19.addWidget(self.label_4)
        self.amountLineEdit = QtWidgets.QLineEdit(self.layoutWidget9)
        self.amountLineEdit.setObjectName("amountLineEdit")
        self.verticalLayout_19.addWidget(self.amountLineEdit)
        self.layoutWidget10 = QtWidgets.QWidget(self.sharePage)
        self.layoutWidget10.setGeometry(QtCore.QRect(470, 230, 201, 41))
        self.layoutWidget10.setObjectName("layoutWidget10")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.layoutWidget10)
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget10)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_20.addWidget(self.label_5)
        self.groupComboBox = QtWidgets.QComboBox(self.layoutWidget10)
        self.groupComboBox.setObjectName("groupComboBox")
        self.verticalLayout_20.addWidget(self.groupComboBox)
        self.tabWidget.addTab(self.sharePage, "")
        self.licensePage = QtWidgets.QWidget()
        self.licensePage.setObjectName("licensePage")
        self.licenseSavePushButton = QtWidgets.QPushButton(self.licensePage)
        self.licenseSavePushButton.setGeometry(QtCore.QRect(634, 70, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.licenseSavePushButton.setFont(font)
        self.licenseSavePushButton.setObjectName("licenseSavePushButton")
        self.licenseSummaryTableWidget = QtWidgets.QTableWidget(self.licensePage)
        self.licenseSummaryTableWidget.setGeometry(QtCore.QRect(5, 110, 761, 401))
        self.licenseSummaryTableWidget.setObjectName("licenseSummaryTableWidget")
        self.licenseSummaryTableWidget.setColumnCount(0)
        self.licenseSummaryTableWidget.setRowCount(0)
        self.permitYearLabel_2 = QtWidgets.QLabel(self.licensePage)
        self.permitYearLabel_2.setGeometry(QtCore.QRect(20, 90, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.permitYearLabel_2.setFont(font)
        self.permitYearLabel_2.setObjectName("permitYearLabel_2")
        self.layoutWidget11 = QtWidgets.QWidget(self.licensePage)
        self.layoutWidget11.setGeometry(QtCore.QRect(10, 10, 151, 46))
        self.layoutWidget11.setObjectName("layoutWidget11")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.layoutWidget11)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.permitYearLabel = QtWidgets.QLabel(self.layoutWidget11)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.permitYearLabel.setFont(font)
        self.permitYearLabel.setObjectName("permitYearLabel")
        self.verticalLayout_12.addWidget(self.permitYearLabel)
        self.licenseYearLineEdit = QtWidgets.QLineEdit(self.layoutWidget11)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.licenseYearLineEdit.setFont(font)
        self.licenseYearLineEdit.setObjectName("licenseYearLineEdit")
        self.verticalLayout_12.addWidget(self.licenseYearLineEdit)
        self.layoutWidget12 = QtWidgets.QWidget(self.licensePage)
        self.layoutWidget12.setGeometry(QtCore.QRect(170, 10, 161, 47))
        self.layoutWidget12.setObjectName("layoutWidget12")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.layoutWidget12)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget12)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_13.addWidget(self.label_6)
        self.licenseAnimalComboBox = QtWidgets.QComboBox(self.layoutWidget12)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.licenseAnimalComboBox.setFont(font)
        self.licenseAnimalComboBox.setObjectName("licenseAnimalComboBox")
        self.verticalLayout_13.addWidget(self.licenseAnimalComboBox)
        self.layoutWidget13 = QtWidgets.QWidget(self.licensePage)
        self.layoutWidget13.setGeometry(QtCore.QRect(340, 10, 141, 46))
        self.layoutWidget13.setObjectName("layoutWidget13")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.layoutWidget13)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget13)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_14.addWidget(self.label_7)
        self.licenseAgeGroupComboBox = QtWidgets.QComboBox(self.layoutWidget13)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.licenseAgeGroupComboBox.setFont(font)
        self.licenseAgeGroupComboBox.setObjectName("licenseAgeGroupComboBox")
        self.verticalLayout_14.addWidget(self.licenseAgeGroupComboBox)
        self.layoutWidget14 = QtWidgets.QWidget(self.licensePage)
        self.layoutWidget14.setGeometry(QtCore.QRect(490, 10, 131, 46))
        self.layoutWidget14.setObjectName("layoutWidget14")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.layoutWidget14)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget14)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_15.addWidget(self.label_8)
        self.licenseGenderComboBox = QtWidgets.QComboBox(self.layoutWidget14)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.licenseGenderComboBox.setFont(font)
        self.licenseGenderComboBox.setObjectName("licenseGenderComboBox")
        self.verticalLayout_15.addWidget(self.licenseGenderComboBox)
        self.layoutWidget15 = QtWidgets.QWidget(self.licensePage)
        self.layoutWidget15.setGeometry(QtCore.QRect(630, 10, 135, 47))
        self.layoutWidget15.setObjectName("layoutWidget15")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.layoutWidget15)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget15)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_16.addWidget(self.label_9)
        self.licenseAmountLineEdit = QtWidgets.QLineEdit(self.layoutWidget15)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.licenseAmountLineEdit.setFont(font)
        self.licenseAmountLineEdit.setObjectName("licenseAmountLineEdit")
        self.verticalLayout_16.addWidget(self.licenseAmountLineEdit)
        self.tabWidget.addTab(self.licensePage, "")
        self.maintenancePage = QtWidgets.QWidget()
        self.maintenancePage.setObjectName("maintenancePage")
        self.layoutWidget16 = QtWidgets.QWidget(self.maintenancePage)
        self.layoutWidget16.setGeometry(QtCore.QRect(10, 10, 751, 501))
        self.layoutWidget16.setObjectName("layoutWidget16")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget16)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_4 = QtWidgets.QGroupBox(self.layoutWidget16)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout.addWidget(self.groupBox_4, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.layoutWidget16)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout.addWidget(self.groupBox, 0, 1, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.layoutWidget16)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout.addWidget(self.groupBox_3, 1, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.layoutWidget16)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout.addWidget(self.groupBox_2, 1, 1, 1, 1)
        self.tabWidget.addTab(self.maintenancePage, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 804, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tabWidget, self.summaryRefreshPushButton)
        MainWindow.setTabOrder(self.summaryRefreshPushButton, self.meatSharedTableWidget)
        MainWindow.setTabOrder(self.meatSharedTableWidget, self.groupSummaryTableWidget)
        MainWindow.setTabOrder(self.groupSummaryTableWidget, self.shotByComboBox)
        MainWindow.setTabOrder(self.shotByComboBox, self.shotDateEdit)
        MainWindow.setTabOrder(self.shotDateEdit, self.locationLineEdit)
        MainWindow.setTabOrder(self.locationLineEdit, self.animalComboBox)
        MainWindow.setTabOrder(self.animalComboBox, self.ageGroupComboBox)
        MainWindow.setTabOrder(self.ageGroupComboBox, self.genderComboBox)
        MainWindow.setTabOrder(self.genderComboBox, self.weightLineEdit)
        MainWindow.setTabOrder(self.weightLineEdit, self.usageComboBox)
        MainWindow.setTabOrder(self.usageComboBox, self.additionalInfoTextEdit)
        MainWindow.setTabOrder(self.additionalInfoTextEdit, self.saveShotPushButton)
        MainWindow.setTabOrder(self.saveShotPushButton, self.killsKillsTableWidget)
        MainWindow.setTabOrder(self.killsKillsTableWidget, self.shareKillsTableWidget)
        MainWindow.setTabOrder(self.shareKillsTableWidget, self.shareDateEdit)
        MainWindow.setTabOrder(self.shareDateEdit, self.portionComboBox)
        MainWindow.setTabOrder(self.portionComboBox, self.amountLineEdit)
        MainWindow.setTabOrder(self.amountLineEdit, self.groupComboBox)
        MainWindow.setTabOrder(self.groupComboBox, self.shareSavePushButton)
        MainWindow.setTabOrder(self.shareSavePushButton, self.licenseYearLineEdit)
        MainWindow.setTabOrder(self.licenseYearLineEdit, self.licenseAnimalComboBox)
        MainWindow.setTabOrder(self.licenseAnimalComboBox, self.licenseAgeGroupComboBox)
        MainWindow.setTabOrder(self.licenseAgeGroupComboBox, self.licenseGenderComboBox)
        MainWindow.setTabOrder(self.licenseGenderComboBox, self.licenseAmountLineEdit)
        MainWindow.setTabOrder(self.licenseAmountLineEdit, self.licenseSavePushButton)
        MainWindow.setTabOrder(self.licenseSavePushButton, self.licenseSummaryTableWidget)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.sharedMeatLabel.setText(_translate("MainWindow", "Jaetut lihat ryhmittäin"))
        self.summaryRefreshPushButton.setText(_translate("MainWindow", "Päivitä"))
        self.groupSummaryLabel.setText(_translate("MainWindow", "Ryhmän tiedot"))
        self.summarySuggestGroupBox.setTitle(_translate("MainWindow", "Ehdotukset"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.summaryPage), _translate("MainWindow", "Yhteenveto"))
        self.saveShotPushButton.setText(_translate("MainWindow", "Tallenna"))
        self.animalLabel.setText(_translate("MainWindow", "Eläin"))
        self.ageGroupLabel.setText(_translate("MainWindow", "Ikäryhmä"))
        self.genderLabel.setText(_translate("MainWindow", "Sukupuoli"))
        self.label.setText(_translate("MainWindow", "Kaadot"))
        self.shotByLabel.setText(_translate("MainWindow", "Kaataja"))
        self.shotDateLabel.setText(_translate("MainWindow", "Kaatopäivä"))
        self.shotDateEdit.setDisplayFormat(_translate("MainWindow", "dd.MM.yyyy"))
        self.locationLabel.setText(_translate("MainWindow", "Paikka"))
        self.locationLineEdit.setToolTip(_translate("MainWindow", "Karttaan merkitty paikan nimi"))
        self.additionalInfoLabel.setText(_translate("MainWindow", "Lisätietoja"))
        self.additionalInfoTextEdit.setToolTip(_translate("MainWindow", "Tähän vieraan kaatajan nimi tai havaintoja eläimestä"))
        self.usageLabel.setText(_translate("MainWindow", "Käyttö"))
        self.weightLabel.setText(_translate("MainWindow", "Paino"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.killPage), _translate("MainWindow", "Kaato"))
        self.shareSavePushButton.setText(_translate("MainWindow", "Tallenna"))
        self.shareSuggestGroupBox.setTitle(_translate("MainWindow", "Jakoehdotukset"))
        self.shareKillsLabel.setText(_translate("MainWindow", "Kaadot"))
        self.shareKillsTableWidget.setToolTip(_translate("MainWindow", "Valitse kaato, jonka lihoja jaetaan"))
        self.label_2.setText(_translate("MainWindow", "Jakopäivä"))
        self.shareDateEdit.setDisplayFormat(_translate("MainWindow", "dd.MM.yyyy"))
        self.label_3.setText(_translate("MainWindow", "Ruhon osa"))
        self.label_4.setText(_translate("MainWindow", "Määrä (kg)"))
        self.label_5.setText(_translate("MainWindow", "Jakoryhmä"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sharePage), _translate("MainWindow", "Lihanjako"))
        self.licenseSavePushButton.setText(_translate("MainWindow", "Tallenna"))
        self.permitYearLabel_2.setText(_translate("MainWindow", "Myönnetyt luvat"))
        self.permitYearLabel.setText(_translate("MainWindow", "Lupavuosi"))
        self.label_6.setText(_translate("MainWindow", "Eläin"))
        self.label_7.setText(_translate("MainWindow", "Ikäryhmä"))
        self.label_8.setText(_translate("MainWindow", "Sukupuoli"))
        self.label_9.setText(_translate("MainWindow", "Määrä"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.licensePage), _translate("MainWindow", "Luvat"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Jäsen"))
        self.groupBox.setTitle(_translate("MainWindow", "Seura"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Jakoryhmä"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Seurue"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.maintenancePage), _translate("MainWindow", "Ylläpito"))
