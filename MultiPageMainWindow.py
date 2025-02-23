# APPLICATION FOR READING DATA FROM A DATABASE AND SHOWING RESULTS IN A MULTI PAGE TAB WIDGET
# ===========================================================================================

# LIBRARIES AND MODULES
# ---------------------

# TODO: flake8 tarkistukset
# flake8 . --max-line-length=127

import sys # Needed for starting the application
import platform  # For detecting operating system for favicon path
from datetime import date

from PyQt5.QtWidgets import QMainWindow, QStatusBar, QApplication  # Needed widgets
# from PyQt5.QtCore import * # All from QtCore
# from PyQt5.QtWidgets import *  # All widgets
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon

# Own modules
import pgModule
import prepareData
import dialogWindows
import figures
import config

# CLASS DEFINITIONS FOR THE APP
# -----------------------------
# TODO: Make UI responsive to resizing
class MultiPageMainWindow(QMainWindow):
    # Constructor, a method for creating objects from this class
    def __init__(self):
        QMainWindow.__init__(self)
    
        # Create an UI from the ui file
        loadUi("QT_UI_files/MultiPageMainWindow.ui", self)
        
        # Set window title
        self.setWindowTitle("Jahtirekisteri")

        currentOS = platform.system()  # MacOS = Darwin
        if currentOS == "Linux" or currentOS == "Darwin":
            self.setWindowIcon(QIcon("docs/Pictures/favicon-64x64.png"))
        else:
            self.setWindowIcon(QIcon("docs\Pictures\\favicon-64x64.png"))


        # Read database connection arguments from the settings file
        databaseOperation = pgModule.DatabaseOperation()
        self.connectionArguments = databaseOperation.readDatabaseSettingsFromFile(config.DBSETTINGS_FILE)

        # UI ELEMENTS TO PROPERTIES
        # -------------------------
        # Set current date when the app starts
        self.currentDate = date.today()

        # Create a status bar to show informative messages (replaces print function used in previous exercises)
        self.statusBar = QStatusBar() # Create a status bar object
        # Set it as the status bar for the main window
        self.setStatusBar(self.statusBar)
        self.statusBar.show() # Make it visible

        # Summary page (Yhteenveto)
        self.openSankeyBtn = self.openSankeyPushButton
        self.openSankeyBtn.clicked.connect(self.openSankey)  # Signal
        self.summaryRefreshBtn = self.summaryRefreshPushButton
        self.summaryRefreshBtn.clicked.connect(self.populateSummaryPage)  # Signal

        self.summaryMeatSharedTW = self.meatSharedTableWidget
        self.summaryGroupSummaryTW = self.groupSummaryTableWidget

        # Kill page (Kaato)
        self.shotByCB = self.shotByComboBox
        self.shotDateDE = self.shotDateEdit
        self.shotLocationLE = self.locationLineEdit
        self.shotAnimalCB = self.animalComboBox
        self.shotAgeGroupCB = self.ageGroupComboBox
        self.shotGenderCB = self.genderComboBox
        self.shotWeightLE = self.weightLineEdit
        self.shotUsageCB = self.usageComboBox
        self.shotAddInfoTE = self.additionalInfoTextEdit
        self.shotSavePushBtn = self.saveShotPushButton
        self.shotSavePushBtn.clicked.connect(self.saveShot) # Signal
        self.shotKillsTW = self.killsKillsTableWidget

        # Share page (Lihanjako)
        self.shareKillsTW = self.shareKillsTableWidget
        self.shareDE = self.shareDateEdit
        self.sharePortionCB = self.portionComboBox
        self.shareAmountLE = self.amountLineEdit
        self.shareGroupCB = self.groupComboBox
        self.shareSavePushBtn = self.shareSavePushButton
        # TODO: Signal for shareSavePushBtn

        # License page (Luvat)
        self.licenseYearLE = self.licenseYearLineEdit
        self.licenseAnimalCB = self.licenseAnimalComboBox
        self.licenseAgeGroupCB = self.licenseAgeGroupComboBox
        self.licenseGenderCB = self.licenseGenderComboBox
        self.licenseAmountLE = self.licenseAmountLineEdit
        self.licenseSavePushBtn = self.licenseSavePushButton
        self.licenseSavePushBtn.clicked.connect(self.saveLicense) # Signal
        self.licenseSummaryTW = self.licenseSummaryTableWidget

        # Administration page (Ylläpito)
        # Member (Jäsen)
        self.admMembFirstNameLE = self.firstNameLineEdit
        self.admMembLastNameLE = self.lastNameLineEdit
        self.admMembAddressLE = self.addressLineEdit
        self.admMembCityLE = self.cityLineEdit
        self.admMembZipCodeLE = self.zipCodeLineEdit
        self.admMembSavePB = self.memberSavePushButton
        self.admMembSavePB.clicked.connect(self.admAddMember) # Signal
        self.admMembDelCB = self.memberDeleteComboBox
        self.admMembDelPB = self.memberDeletePushButton
        self.admMembDelPB.clicked.connect(self.admDelMember) # Signal
        self.admMembRestoreCB = self.memberRestoreComboBox
        self.admMembRestorePB = self.memberRestorePushButton
        self.admMembRestorePB.clicked.connect(self.admRestoreMember) # Signal

        # TODO: Create manual dialog (current is a placeholder)
        # No idea for manual yet. HTML file?.. Maybe PDF file.

        # Actions
        # Menu: Tietokanta > Palvelinasetukset...
        self.actionServerSettings.triggered.connect(self.openSettingsDialog)
        
        # Menu: Tietoa > Ohjelma...
        self.actionAboutProgram.triggered.connect(self.openAboutDialog)

        # Menu: Tietoa > Käyttöohje...
        self.actionManual.triggered.connect(self.openManualDialog)

        # Signal when a page is opened
        self.pageTab = self.tabWidget
        self.pageTab.currentChanged.connect(self.pageChanged, self.pageTab.currentIndex())

        # Signals other than emitted by UI elements
        self.populateAllPages()

    # SLOTS
    # Modify and save database settings - Tietokanta > Palvelinasetukset...
    def openSettingsDialog(self):
        dialog = dialogWindows.DBSettingsDialog()
        dialog.exec()

    # Menu: Tietoa > Ohjelma...
    def openAboutDialog(self):
        dialog = dialogWindows.AboutDialog()
        dialog.exec()

    # Menu: Tietoa > Käyttöohje...
    def openManualDialog(self):
        dialog = dialogWindows.ManualDialog()
        dialog.exec()

    def openSankey(self):
        # TODO: Set real database data to sankey-diagram (currently only shows random test-data)
        htmlFile = 'meatstreams.html'
        urlString = f'file:///{htmlFile}'

        figure = figures.testChart()
        figures.createOfflineFile(figure, htmlFile) # Write the chart to a html file

    # A method to populate summaryPage's table widgets
    def populateSummaryPage(self):
        # Read data from view jaetut_lihat
        databaseOperation1 = pgModule.DatabaseOperation()
        databaseOperation1.getAllRowsFromTable(self.connectionArguments, "public.jaetut_lihat")

        # Check if error has occured
        if databaseOperation1.errorCode != 0:
            dialogWindows.alert('Vakava virhe', 'Tietokantaoperaatio epäonnistui', 
            databaseOperation1.errorMessage, databaseOperation1.detailedMessage)
        else:
            prepareData.prepareTable(databaseOperation1, self.summaryMeatSharedTW)

        # Read data from view jakoryhma_yhteenveto, no need to read con args twice
        databaseOperation2 = pgModule.DatabaseOperation()
        databaseOperation2.getAllRowsFromTable(self.connectionArguments, 'public.jakoryhma_yhteenveto')

        # Check if error has occured
        if databaseOperation2.errorCode != 0:
            dialogWindows.alert('Vakava virhe', 'Tietokantaoperaatio epäonnistui', 
            databaseOperation2.errorMessage, databaseOperation2.detailedMessage)
        else:
            prepareData.prepareTable(databaseOperation2, self.summaryGroupSummaryTW)

    def populateKillPage(self):
        # Set default date to current date
        self.shotDateDE.setDate(self.currentDate)
        # Read data from view kaatoluettelo
        databaseOperation1 = pgModule.DatabaseOperation()
        databaseOperation1.getAllRowsFromTable(self.connectionArguments, "public.kaatoluettelo")

        # Check if error has occured
        if databaseOperation1.errorCode != 0:
            dialogWindows.alert('Vakava virhe', 'Tietokantaoperaatio epäonnistui', 
            databaseOperation1.errorMessage, databaseOperation1.detailedMessage)
        else:
            prepareData.prepareTable(databaseOperation1, self.shotKillsTW)

        # Read data from view nimivalinta
        databaseOperation2 = pgModule.DatabaseOperation()
        databaseOperation2.getAllRowsFromTable(self.connectionArguments, "public.nimivalinta")

        # Check if error has occured
        if databaseOperation2.errorCode != 0:
            dialogWindows.alert('Vakava virhe', 'Tietokantaoperaatio epäonnistui', 
            databaseOperation2.errorMessage, databaseOperation2.detailedMessage)
        else: 
            self.shotByIdList = prepareData.prepareComboBox(databaseOperation2, self.shotByCB, 1, 0)
        
        # Read data from table elain and populate the combo box
        databaseOperation3 = pgModule.DatabaseOperation()
        databaseOperation3.getAllRowsFromTable(self.connectionArguments, 'public.elain')

        # Check if error has occured
        if databaseOperation3.errorCode != 0:
            dialogWindows.alert('Vakava virhe', 'Tietokantaoperaatio epäonnistui', 
            databaseOperation3.errorMessage, databaseOperation3.detailedMessage)
        else:
            self.shotAnimalText = prepareData.prepareComboBox(databaseOperation3, self.shotAnimalCB, 0, 0)

        # Read data from table aikiunenvasa and populate the combo box
        databaseOperation4 = pgModule.DatabaseOperation()
        databaseOperation4.getAllRowsFromTable(self.connectionArguments, 'public.aikuinenvasa')

        # Check if error has occured
        if databaseOperation4.errorCode != 0:
            dialogWindows.alert('Vakava virhe', 'Tietokantaoperaatio epäonnistui', 
            databaseOperation4.errorMessage, databaseOperation4.detailedMessage)
        else:
            self.shotAgeGroupText = prepareData.prepareComboBox(databaseOperation4, self.shotAgeGroupCB, 0, 0)

        # Read data from table sukupuoli and populate the combo box
        databaseOperation5 = pgModule.DatabaseOperation()
        databaseOperation5.getAllRowsFromTable(self.connectionArguments, 'public.sukupuoli')

        # Check if error has occured
        if databaseOperation5.errorCode != 0:
            dialogWindows.alert('Vakava virhe', 'Tietokantaoperaatio epäonnistui', 
            databaseOperation5.errorMessage, databaseOperation5.detailedMessage)
        else:
            self.shotGenderText = prepareData.prepareComboBox(databaseOperation5, self.shotGenderCB, 0, 0)

        # Read data from table kasittely and populate the combo box
        databaseOperation6 = pgModule.DatabaseOperation()
        databaseOperation6.getAllRowsFromTable(self.connectionArguments, 'public.kasittely')

        # Check if error has occured
        if databaseOperation6.errorCode != 0:
            dialogWindows.alert('Vakava virhe', 'Tietokantaoperaatio epäonnistui', 
            databaseOperation6.errorMessage, databaseOperation6.detailedMessage)
        else:
            self.shotUsageIdList = prepareData.prepareComboBox(databaseOperation6, self.shotUsageCB, 1, 0)

    def populateSharePage(self):
        # Set default date to current date
        self.shareDE.setDate(self.currentDate)
        # Read data from view kaatoluettelo
        databaseOperation1 = pgModule.DatabaseOperation()
        databaseOperation1.getAllRowsFromTable(self.connectionArguments, "public.kaatoluettelo")

        # Check if error has occured
        if databaseOperation1.errorCode != 0:
            dialogWindows.alert('Vakava virhe', 'Tietokantaoperaatio epäonnistui', 
            databaseOperation1.errorMessage, databaseOperation1.detailedMessage)
        else:
            prepareData.prepareTable(databaseOperation1, self.shareKillsTW)

        # Read data from table ruhonosa
        databaseOperation2 = pgModule.DatabaseOperation()
        databaseOperation2.getAllRowsFromTable(self.connectionArguments, "public.ruhonosa")

        # Check if error has occured
        if databaseOperation2.errorCode != 0:
            dialogWindows.alert('Vakava virhe', 'Tietokantaoperaatio epäonnistui', 
            databaseOperation2.errorMessage, databaseOperation2.detailedMessage)
        else: 
            self.sharePortionText = prepareData.prepareComboBox(databaseOperation2, self.sharePortionCB, 0, 0)

        # Read data from table jakoryhma
        databaseOperation3 = pgModule.DatabaseOperation()
        databaseOperation3.getAllRowsFromTable(self.connectionArguments, "public.jakoryhma")

        # Check if error has occured
        if databaseOperation3.errorCode != 0:
            dialogWindows.alert('Vakava virhe', 'Tietokantaoperaatio epäonnistui', 
            databaseOperation3.errorMessage, databaseOperation3.detailedMessage)
        else: 
            self.shareGroupIdList = prepareData.prepareComboBox(databaseOperation3, self.shareGroupCB, 2, 0)

    def populateLicensePage(self):
        # Set default license year to current year
        self.licenseYearLE.setText(str(self.currentDate.year))

        # Read data from table lupa
        databaseOperationLuvat = pgModule.DatabaseOperation()
        databaseOperationLuvat.getAllRowsFromTable(self.connectionArguments, "public.lupalista")

        # Check if error has occured
        if databaseOperationLuvat.errorCode != 0:
            dialogWindows.alert('Vakava virhe', 'Tietokantaoperaatio epäonnistui', 
            databaseOperationLuvat.errorMessage, databaseOperationLuvat.detailedMessage)
        else:
            prepareData.prepareTable(databaseOperationLuvat, self.licenseSummaryTW)

        # Read data from table elain
        databaseOperation1 = pgModule.DatabaseOperation()
        databaseOperation1.getAllRowsFromTable(self.connectionArguments, "public.elain")

        # Check if error has occured
        if databaseOperation1.errorCode != 0:
            dialogWindows.alert('Vakava virhe', 'Tietokantaoperaatio epäonnistui', 
            databaseOperation1.errorMessage, databaseOperation1.detailedMessage)
        else:
            self.licenseAnimalText = prepareData.prepareComboBox(databaseOperation1, self.licenseAnimalCB, 0, 0)

        # Read data from table aikuinenvasa (age group)
        databaseOperation2 = pgModule.DatabaseOperation()
        databaseOperation2.getAllRowsFromTable(self.connectionArguments, "public.aikuinenvasa")

        # Check if error has occured
        if databaseOperation2.errorCode != 0:
            dialogWindows.alert('Vakava virhe', 'Tietokantaoperaatio epäonnistui', 
            databaseOperation2.errorMessage, databaseOperation2.detailedMessage)
        else: 
            self.licenseAgeGroupText = prepareData.prepareComboBox(databaseOperation2, self.licenseAgeGroupCB, 0, 0)

        # Read data from table sukupuoli
        databaseOperation3 = pgModule.DatabaseOperation()
        databaseOperation3.getAllRowsFromTable(self.connectionArguments, "public.sukupuoli")
        
        # Check if error has occured
        if databaseOperation3.errorCode != 0:
            dialogWindows.alert('Vakava virhe', 'Tietokantaoperaatio epäonnistui', 
            databaseOperation3.errorMessage, databaseOperation3.detailedMessage)
        else: 
            self.licenseGenderText = prepareData.prepareComboBox(databaseOperation3, self.licenseGenderCB, 0, 0)
    
    def populateAdminPage(self):
        # Populate removable member combobox
        databaseOperation1 = pgModule.DatabaseOperation()
        databaseOperation1.getAllRowsFromTable(self.connectionArguments, "public.nimivalinta")
        # Check if error has occured
        if databaseOperation1.errorCode != 0:
            dialogWindows.alert('Vakava virhe', 'Tietokantaoperaatio epäonnistui', 
            databaseOperation1.errorMessage, databaseOperation1.detailedMessage)
        else:
            self.admPageMembersIdList = prepareData.prepareComboBox(databaseOperation1, self.admMembDelCB, 1, 0)

        # Populate restorable member combobox
        databaseOperation2 = pgModule.DatabaseOperation()
        databaseOperation2.getAllRowsFromTable(self.connectionArguments, "public.nimivalinta_inaktiiviset")
        # Check if error has occured
        if databaseOperation2.errorCode != 0:
            dialogWindows.alert('Vakava virhe', 'Tietokantaoperaatio epäonnistui', 
            databaseOperation2.errorMessage, databaseOperation2.detailedMessage)
        else:
            self.admPageInactiveMembersIdList = prepareData.prepareComboBox(databaseOperation2, self.admMembRestoreCB, 1, 0)

    def populateAllPages(self):
        self.populateSummaryPage()
        self.populateKillPage()
        self.populateSharePage()
        self.populateLicensePage()
        self.populateAdminPage()

    def pageChanged(self, index):
        # Yhteenveto = 0
        # Kaato = 1
        # Lihanjako = 2
        # Luvat = 3
        # Ylläpito = 4
        if index == 0:
            self.populateSummaryPage()
        elif index == 1:
            self.populateKillPage()
        elif index == 2:
            self.populateSharePage()
        elif index == 3:
            self.populateLicensePage()
        elif index == 4:
            self.populateAdminPage()
        
        # Testi:
        # QMessageBox.information(self,
        #     "Tab Index Changed!",
        #     "Current Tab Index: " + str(index)) #changed!

    def saveShot(self):
        errorOccured = False
        try:
            shotByChosenItemIx = self.shotByCB.currentIndex()
            shotById = self.shotByIdList[shotByChosenItemIx]
            shootingDay = self.shotDateDE.date().toPyDate()
            shootingPlace = self.shotLocationLE.text()
            animal = self.shotAnimalCB.currentText()
            ageGroup = self.shotAgeGroupCB.currentText()
            gender = self.shotGenderCB.currentText()
            weight = float(self.shotWeightLE.text())
            useIx = self.shotUsageCB.currentIndex()
            use = self.shotUsageIdList[useIx]
            additionalInfo = self.shotAddInfoTE.toPlainText()

            # Insert data into kaato table
            sqlClauseBeginning = "INSERT INTO public.kaato(\
                jasen_id, kaatopaiva, ruhopaino, paikka_teksti,\
                kasittelyid, elaimen_nimi, sukupuoli, ikaluokka, lisatieto)\
                VALUES ("
            sqlClauseValues = f"""
                {shotById}, '{shootingDay}', {weight}, '{shootingPlace}', {use},
                '{animal}', '{gender}', '{ageGroup}', '{additionalInfo}'"""
            sqlClauseEnd = ");"
            sqlClause = sqlClauseBeginning + sqlClauseValues + sqlClauseEnd

        # Check for conversion errors
        except Exception as error:
            errorOccured = True
            dialogWindows.alert('Virheellinen syöte', 'Tarkista antamasi tiedot', 'Tyyppivirhe', str(error))
        finally:
            if not errorOccured:
                print(sqlClause)
                # Create DatabaseOperation object to execute the SQL clause
                databaseOperation = pgModule.DatabaseOperation()
                databaseOperation.insertRowToTable(self.connectionArguments, sqlClause)
                
                if databaseOperation.errorCode != 0:
                    dialogWindows.alert('Vakava virhe', 'Tietokantaoperaatio epäonnistui',
                        databaseOperation.errorMessage, databaseOperation.detailedMessage)
                else:
                    # Update the page to show new data and clear previous data from elements
                    self.populateKillPage()
                    self.shotLocationLE.clear()
                    self.shotWeightLE.clear()
                    self.shotAddInfoTE.clear()
                    # self.shotDateDE

                # print('ampujan id:', shotById, '---', 'ampumispäivä:', shootingDay)
                # print('paikka:', shootingPlace, 'elukka:', animal, ageGroup, gender)

                # paino, käyttö, lisätietoja

    def saveLicense(self):
        errorOccured = False
        try:
            lYear = int(self.licenseYearLE.text())
            lAnimal = self.licenseAnimalCB.currentText()
            lAgeGroup = self.licenseAgeGroupCB.currentText()
            lGender = self.licenseGenderCB.currentText()
            lAmount = int(self.licenseAmountLE.text())

            """
                self.licenseSavePushBtn = self.licenseSavePushButton
                self.licenseSavePushBtn.clicked.connect(self.saveLicense) # Signal
                self.licenseSummaryTW = self.licenseSummaryTableWidget
            """
            # Insert data into license table
            sqlClauseBeginning = "INSERT INTO public.lupa(\
                seura_id, lupavuosi, elaimen_nimi, sukupuoli,\
                ikaluokka, maara)\
                VALUES ("
            # TODO: seura_id is set to 1. assuming there is only one seura.
            # There is no ui element to choose a seura from.
            sqlClauseValues = f"1, {lYear}, '{lAnimal}', '{lGender}', '{lAgeGroup}', {lAmount}"
            sqlClauseEnd = ");"
            sqlClause = sqlClauseBeginning + sqlClauseValues + sqlClauseEnd
        except Exception as error:
            errorOccured = True
            dialogWindows.alert('Virheellinen syöte', 'Tarkista antamasi tiedot', 'Tyyppivirhe', str(error))
        finally:
            if not errorOccured:
                print(sqlClause)
                # Create DatabaseOperation object to execute the SQL clause
                databaseOperation = pgModule.DatabaseOperation()
                databaseOperation.insertRowToTable(self.connectionArguments, sqlClause)
                
                if databaseOperation.errorCode != 0:
                    dialogWindows.alert('Vakava virhe', 'Tietokantaoperaatio epäonnistui',
                        databaseOperation.errorMessage, databaseOperation.detailedMessage)
                else:
                    # Update the page to show new data and clear previous data from elements
                    self.populateLicensePage()
                    self.licenseYearLE.clear()
                    self.licenseAnimalCB.clear()
                    self.licenseAgeGroupCB.clear()
                    self.licenseGenderCB.clear()
                    self.licenseAmountLE.clear()

    def admAddMember(self):
        errorOccured = False
        try:
            membFirstName = self.admMembFirstNameLE.text()
            membLastName = self.admMembLastNameLE.text()
            membAddress = self.admMembAddressLE.text()
            membCity = self.admMembCityLE.text()
            membZipCode = self.admMembZipCodeLE.text()

            # Insert data into jasen table
            sqlClause = f"""INSERT INTO public.jasen(
                etunimi, sukunimi, jakeluosoite, postinumero,
                postitoimipaikka, tila)
                VALUES (
                '{membFirstName}', '{membLastName}', '{membAddress}', '{membZipCode}',
                '{membCity}', 'aktiivinen');
            """
        except Exception as error:
            errorOccured = True
            dialogWindows.alert('Virhe', 'Tarkista antamasi tiedot', 'Tyyppivirhe', str(error))
        finally:
            if not errorOccured:
                # Create DatabaseOperation object to execute the SQL clause
                databaseOperation = pgModule.DatabaseOperation()
                databaseOperation.insertRowToTable(self.connectionArguments, sqlClause)
                
                if databaseOperation.errorCode != 0:
                    dialogWindows.alert('Vakava virhe', 'Tietokantaoperaatio epäonnistui',
                        databaseOperation.errorMessage, databaseOperation.detailedMessage)
                else:
                    # Update the page to show new data and clear previous data from elements
                    self.populateAdminPage()
                    self.admMembFirstNameLE.clear()
                    self.admMembLastNameLE.clear()
                    self.admMembAddressLE.clear()
                    self.admMembCityLE.clear()
                    self.admMembZipCodeLE.clear()

    def admDelMember(self):
        admMembDelCBItemIx = self.admMembDelCB.currentIndex()
        memberToDeleteId = self.admPageMembersIdList[admMembDelCBItemIx]

        # Create DatabaseOperation object to execute the SQL clause
        databaseOperation = pgModule.DatabaseOperation()
        databaseOperation.updateTable(
            self.connectionArguments, "public.jasen", "tila = 'inaktiivinen'", 
            f'jasen_id = {memberToDeleteId}'
        )

        # Vanha koodi jolla poistettiin jäsen kokonaan
        # databaseOperation.deleteFromTable(
        #     self.connectionArguments, "public.jasen", 
        #     f"jasen_id = {memberToDeleteId}"
        # )

        if databaseOperation.errorCode != 0:
            dialogWindows.alert('Vakava virhe', 'Tietokantaoperaatio epäonnistui',
            databaseOperation.errorMessage, databaseOperation.detailedMessage)
        else:
            # Update the page to show new data
            self.populateAdminPage()

    def admRestoreMember(self):
        admMembRestoreCBItemIx = self.admMembRestoreCB.currentIndex()
        memberToRestoreId = self.admPageInactiveMembersIdList[admMembRestoreCBItemIx]

        # Create DatabaseOperation object to execute the SQL clause
        databaseOperation = pgModule.DatabaseOperation()
        databaseOperation.updateTable(
            self.connectionArguments, "public.jasen", "tila = 'aktiivinen'", 
            f'jasen_id = {memberToRestoreId}'
        )
        if databaseOperation.errorCode != 0:
            dialogWindows.alert('Vakava virhe', 'Tietokantaoperaatio epäonnistui',
            databaseOperation.errorMessage, databaseOperation.detailedMessage)
        else:
            # Update the page to show new data
            self.populateAdminPage()

# APPLICATION CREATION AND STARTING
# ---------------------------------
if __name__ == "__main__":
    # Create an application object
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    # Create the Main Window object from 
    appWindow = MultiPageMainWindow()
    appWindow.show()
    sys.exit(app.exec_())