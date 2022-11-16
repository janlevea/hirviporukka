# APPLICATION FOR SHOWING SUMMARY DATA ABOUT MEAT GIVEN TO SHARE GROUP
# ====================================================================

# LIBRARIES AND MODULES
# ---------------------

import sys # Needed for starting the application
from PyQt5.QtWidgets import * # All widgets
from PyQt5.uic import loadUi
from PyQt5.QtCore import * # FIXME: Everything, change to invidual components 
# Own modules
import pgModule
import prepareData

# CLASS DEFINITIONS FOR THE APP
# -----------------------------
class MultiPageMainWindow(QMainWindow):
    # Constructor, a method for creating objects from this class
    def __init__(self):
        QMainWindow.__init__(self)
    
        # Create an UI from the ui file
        loadUi("MultiPageMainWindow.ui", self)

        # UI ELEMENTS TO PROPERTIES
        # -------------------------
        # Summary page (Yhteenveto)
        self.summaryRefreshBtn = self.summaryRefreshPushButton
        self.summaryRefreshBtn.clicked.connect(self.populateSummaryPage) # Signal

        self.summaryMeatSharedTW = self.meatSharedTableWidget
        self.summaryGroupSummaryTW = self.groupSummaryTableWidget

        # Kill page (Kaato)
        self.shotCB = self.shotByComboBox
        self.shotDate = self.shotDateEdit
        self.shotLocation = self.locationLineEdit
        self.shotAnimalCB = self.animalComboBox
        self.ageGroupCB = self.ageGroupComboBox
        self.genderCB = self.genderComboBox
        self.weightLE = self.weightLineEdit
        self.usageCB = self.usageComboBox
        self.addInfoTE = self.additionalInfoTextEdit
        self.saveShotPushBtn = self.saveShotPushButton
        self.killsKillsTW = self.killsKillsTableWidget

        # Share page (Lihanjako)
        self.shareKillsTW = self.shareKillsTableWidget
        self.shareDE = self.shareDateEdit
        self.portionCB = self.portionComboBox
        self.amountLE = self.amountLineEdit
        self.groupCB = self.groupComboBox
        self.shareSavePushBtn = self.shareSavePushButton

        # License page (Luvat)
        self.licenseYearLE = self.licenseYearLineEdit
        self.licenseAnimalCB = self.licenseAnimalComboBox
        self.licenseAgeGroupCB = self.licenseAgeGroupComboBox
        self.licenseGenderCB = self.licenseGenderComboBox
        self.licenseAmountLE = self.licenseAmountLineEdit
        self.licenseSavePushBtn = self.licenseSavePushButton
        self.licenseSummaryTW = self.licenseSummaryTableWidget

        '''
        # Database connection parameters
        self.database = "metsastys"
        self.user = "sovellus"
        self.userPassword = "Q2werty"
        self.server = "localhost"
        self.port = "5432"
        '''
        # Other signals

    # SLOTS

    # A method to populate summaryPage's table widgets
    def populateSummaryPage(self):
        # Read data from view jaetut_lihat
        databaseOperation1 = pgModule.DatabaseOperation()
        connectionArguments = databaseOperation1.readDatabaseSettingsFromFile('settings.dat')
        databaseOperation1.getAllRowsFromTable(connectionArguments, "public.jaetut_lihat")
        # TODO: MessageBox if an error occured

        # Read data from view jakoryhma_yhteenveto, no need to read con args twice
        databaseOperation2 = pgModule.DatabaseOperation()
        databaseOperation2 = databaseOperation2.getAllRowsFromTable(connectionArguments, 'public.jakoryhma_yhteenveto')
        # TODO: MessageBox if an error occured

        # Let's call the real method which updates the widget
        self.refreshData(databaseOperation1, self.summaryMeatSharedTW)
        self.refreshData(databaseOperation2, self.summaryGroupSummaryTW)


    # This is a function that updates table widgets in the UI
    # because it does not receive signals; it's not a slot
    def refreshData(self, databaseOperation, widget):
        prepareData.prepareTable(databaseOperation, widget)

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