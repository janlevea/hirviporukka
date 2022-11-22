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
        self.shotAgeGroupCB = self.ageGroupComboBox
        self.shotGenderCB = self.genderComboBox
        self.shotWeightLE = self.weightLineEdit
        self.shotUsageCB = self.usageComboBox
        self.shotAddInfoTE = self.additionalInfoTextEdit
        self.shotSavePushBtn = self.saveShotPushButton
        self.shotKillsTW = self.killsKillsTableWidget

        # Share page (Lihanjako)
        self.shareKillsTW = self.shareKillsTableWidget
        self.shareDE = self.shareDateEdit
        self.sharePortionCB = self.portionComboBox
        self.shareAmountLE = self.amountLineEdit
        self.shareGroupCB = self.groupComboBox
        self.shareSavePushBtn = self.shareSavePushButton

        # License page (Luvat)
        self.licenseYearLE = self.licenseYearLineEdit
        self.licenseAnimalCB = self.licenseAnimalComboBox
        self.licenseAgeGroupCB = self.licenseAgeGroupComboBox
        self.licenseGenderCB = self.licenseGenderComboBox
        self.licenseAmountLE = self.licenseAmountLineEdit
        self.licenseSavePushBtn = self.licenseSavePushButton
        self.licenseSummaryTW = self.licenseSummaryTableWidget

        # Signal when a page is opened
        self.pageTab = self.tabWidget
        self.pageTab.currentChanged.connect(self.populateAllPages)

        # Signals other than emitted by UI elements
        self.populateAllPages()

    # SLOTS

    # A method to populate summaryPage's table widgets
    def populateSummaryPage(self):
        # Read data from view jaetut_lihat
        databaseOperation1 = pgModule.DatabaseOperation()
        connectionArguments = databaseOperation1.readDatabaseSettingsFromFile('settings.dat')
        databaseOperation1.getAllRowsFromTable(connectionArguments, "public.jaetut_lihat")
        prepareData.prepareTable(databaseOperation1, self.summaryMeatSharedTW)
        # TODO: MessageBox if an error occured

        # Read data from view jakoryhma_yhteenveto, no need to read con args twice
        databaseOperation2 = pgModule.DatabaseOperation()
        databaseOperation2.getAllRowsFromTable(connectionArguments, 'public.jakoryhma_yhteenveto')
        prepareData.prepareTable(databaseOperation2, self.summaryGroupSummaryTW)
        # TODO: MessageBox if an error occured

    def populateKillPage(self):
        # Read data from view kaatoluettelo
        databaseOperation1 = pgModule.DatabaseOperation()
        connectionArguments = databaseOperation1.readDatabaseSettingsFromFile('settings.dat')
        databaseOperation1.getAllRowsFromTable(connectionArguments, "public.kaatoluettelo")
        prepareData.prepareTable(databaseOperation1, self.shotKillsTW)
        # TODO: MessageBox if an error occured

        # Read data from view nimivalinta
        databaseOperation2 = pgModule.DatabaseOperation()
        databaseOperation2.getAllRowsFromTable(connectionArguments, "public.nimivalinta")
        self.shotById = prepareData.prepareComboBox(databaseOperation2, self.shotCB, 1, 0)
        
        # Read data from table elain and populate the combo box
        databaseOperation3 = pgModule.DatabaseOperation()
        databaseOperation3.getAllRowsFromTable(connectionArguments, 'public.elain')
        self.shotAnimalText = prepareData.prepareComboBox(databaseOperation3, self.shotAnimalCB, 0, 0)

        # Read data from table aikiunenvasa and populate the combo box
        databaseOperation4 = pgModule.DatabaseOperation()
        databaseOperation4.getAllRowsFromTable(connectionArguments, 'public.aikuinenvasa')
        self.shotAgeGroupText = prepareData.prepareComboBox(databaseOperation4, self.shotAgeGroupCB, 0, 0)

        # Read data from table sukupuoli and populate the combo box
        databaseOperation5 = pgModule.DatabaseOperation()
        databaseOperation5.getAllRowsFromTable(connectionArguments, 'public.sukupuoli')
        self.shotGenderText = prepareData.prepareComboBox(databaseOperation5, self.shotGenderCB, 0, 0)

        # Read data from table kasittely and populate the combo box
        databaseOperation6 = pgModule.DatabaseOperation()
        databaseOperation6.getAllRowsFromTable(connectionArguments, 'public.kasittely')
        self.shotUsageId = prepareData.prepareComboBox(databaseOperation6, self.shotUsageCB, 1, 0)


    def populateAllPages(self):
        self.populateSummaryPage()
        self.populateKillPage()


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