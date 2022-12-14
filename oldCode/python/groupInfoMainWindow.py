# APPLICATION FOR SHOWING SUMMARY DATA ABOUT MEAT GIVEN TO SHARE GROUP
# ====================================================================

# LIBRARIES AND MODULES
# ---------------------

import sys # Needed for starting the application
from PyQt5.QtWidgets import * # All widgets
from PyQt5.uic import loadUi
import ui_groupInfoMainWindow

import pgModule
import prepareData
import config

# CLASS DEFINITIONS FOR THE APP
# -----------------------------
class GroupMainWindow(QMainWindow):
    # Constructor, a method for creating objects from this class
    def __init__(self):
        QMainWindow.__init__(self)
    
        # Create an UI from the ui file
        loadUi("groupInfoMainWindow.ui", self)

        # Define properties for ui elements
        self.refreshBtn = self.refreshPushButton
        self.groupInfo = self.groupSummaryTableWidget
        self.sharedMeatInfo = self.meatSharedTableWidget

        '''
        # Database connection parameters
        self.database = "metsastys"
        self.user = "sovellus"
        self.userPassword = "Q2werty"
        self.server = "localhost"
        self.port = "5432"
        '''

        # SIGNALS
        # Emit a signal when refresh push button is pressed
        self.refreshBtn.clicked.connect(self.agentRefreshData)

    # SLOTS

    # Agent method is used for receiving a signal from an UI element
    def agentRefreshData(self):
        # Read data from view jaetut_lihat
        databaseOperation1 = pgModule.DatabaseOperation()
        connectionArguments = databaseOperation1.readDatabaseSettingsFromFile(config.DBSETTINGS_FILE)
        databaseOperation1.getAllRowsFromTable(connectionArguments, "public.jaetut_lihat")

        # Read data from view jakoryhma_yhteenveto, no need to read con args twice
        databaseOperation2 = pgModule.DatabaseOperation()
        databaseOperation2 = databaseOperation2.getAllRowsFromTable(connectionArguments, 'public.jakoryhma_yhteenveto')

        # Let's call the real method which updates the widget
        self.refreshData(databaseOperation1, self.sharedMeatInfo)
        self.refreshData(databaseOperation2, self.groupInfo)

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
    appWindow = GroupMainWindow()
    appWindow.show()
    sys.exit(app.exec_())