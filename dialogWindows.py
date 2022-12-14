import sys
import platform  # Detect operating system for favicon path

from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.uic import loadUi

import pgModule
import config

# Create an alert dialog for critical failures, eg no database connection established
def alert(windowTitle, alertMsg, additionalMsg, details):
    """Creates a message box for critical errors

    Args:
        windowTitle (str): Title of the message box
        alertMsg (str): Short description of the error in finnish
        additionalMsg (str): Additional information in finnish
        details (str): Details about the error in english
    """
    alertDialog = QMessageBox() # Create a message box object
    alertDialog.setWindowTitle(windowTitle) # Add appropriate title to the message box
    alertDialog.setIcon(QMessageBox.Critical) # Set icon to critical
    alertDialog.setText(alertMsg) # Basic information about the error in Finnish
    alertDialog.setInformativeText(additionalMsg) # Additional information about the error in Finnish
    alertDialog.setDetailedText(details) # Technical details in English (from psycopg2)
    alertDialog.setStandardButtons(QMessageBox.Ok) # Only OK is needed to close the dialog
    alertDialog.exec_() # Open the message box

class DialogTestMainWindow(QMainWindow):
    """Main Window for testing dialogs"""
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Pääikkuna dialogien testaukseen')

        # Add dialogs to be tested here and run them as follows

        # dbSettingsDialog = DBSettingsDialog()
        # dbSettingsDialog.exec()

        # aboutDialog = AboutDialog()
        # aboutDialog.exec()

        # manualDialog = ManualDialog()
        # manualDialog.exec()

# A class for a dialog to save database settings
class DBSettingsDialog(QDialog):
    """Creates a dialog to save database settings"""

    # Constructor
    def __init__(self):
        super().__init__()

        loadUi("QT_UI_files/serverSettingsDialog.ui", self)

        self.setWindowTitle('Tietokantapalvelimen asetukset')

        currentOS = platform.system()  # MacOS = Darwin
        if currentOS == "Linux" or currentOS == "Darwin":
            self.setWindowIcon(QIcon("docs/Pictures/favicon-64x64.png"))
        else:
            self.setWindowIcon(QIcon("docs\Pictures\\favicon-64x64.png"))

        # Elements
        self.hostLE = self.serverHostLineEdit
        self.portSB = self.serverPortSpinBox
        self.savePB = self.serverSavePushButton
        self.cancelPB = self.serverCancelPushButton
        self.databaseLE = self.databaseNameLineEdit
        self.usernameLE = self.databaseUserLineEdit
        self.passwordLE = self.databasePasswordLineEdit
        self.fileNameLE = self.fileNameLineEdit

        # Set values of elements according to the current settings
        # Create an object to use setting methods
        self.databaseOperation = pgModule.DatabaseOperation() # Needed in slots -> self
        currentSettings = self.databaseOperation.readDatabaseSettingsFromFile(
            config.DBSETTINGS_FILE)  # Read current settings, needed only in the constructor
        self.hostLE.setText(currentSettings['server'])  # Server's host name
        # Port number, spin box uses integer values
        self.portSB.setValue(int(currentSettings['port']))

        self.databaseLE.setText(currentSettings['database'])
        self.usernameLE.setText(currentSettings['user'])
        self.passwordLE.setText("")
        self.passwordLE.setEchoMode(QLineEdit.Password)

        self.fileNameLE.setText(config.DBSETTINGS_FILE)

        # Signals
        self.savePB.clicked.connect(self.saveSettings)
        self.cancelPB.clicked.connect(self.closeDialog)

    # --- Slots

    # Tallenna button saves modified settings to a file and closes the dialog
    def saveSettings(self):
        server = self.hostLE.text()
        # Port is string in the settings file, integer in the spin box
        port = str(self.portSB.value())

        database = self.databaseLE.text()
        user = self.usernameLE.text()

        password = self.passwordLE.text()

        # Build new connection arguments
        newSettings = self.databaseOperation.createConnectionArgumentDict(
            database, user, password, server, port)
        
        # Save arguments to a json file
        self.databaseOperation.saveDatabaseSettingsToFile(
            config.DBSETTINGS_FILE, newSettings)
        self.close()

    # Peru button closes the dialog
    def closeDialog(self):
        self.close()

# A class for about dialog
class AboutDialog(QDialog):
    """Creates about dialog"""

    # Constructor
    def __init__(self):
        super().__init__()

        loadUi("QT_UI_files/aboutDialog.ui", self)

        self.setWindowTitle('Tietoa ohjelmasta')

        currentOS = platform.system()  # MacOS = Darwin
        if currentOS == "Linux" or currentOS == "Darwin":
            self.setWindowIcon(QIcon("docs/Pictures/favicon-64x64.png"))
        else:
            self.setWindowIcon(QIcon("docs\Pictures\\favicon-64x64.png"))

        # Elements
        self.closePB = self.closePushButton

        # Signals
        self.closePB.clicked.connect(self.closeDialog)

    # Slots
    # Sulje button closes the dialog
    def closeDialog(self):
        self.close()

# A class for manual dialog
# TODO: Create manual dialog.. or open manual in web browser (better for Linux)
# This is only a placeholder, with logo and close button.
class ManualDialog(QDialog):
    """Creates manual dialog"""

    # Constructor
    def __init__(self):
        super().__init__()

        loadUi("QT_UI_files/manualDialog.ui", self)

        self.setWindowTitle('Käyttöohje')
        
        currentOS = platform.system()  # MacOS = Darwin
        if currentOS == "Linux" or currentOS == "Darwin":
            self.setWindowIcon(QIcon("docs/Pictures/favicon-64x64.png"))
        else:
            self.setWindowIcon(QIcon("docs\Pictures\\favicon-64x64.png"))

        # Elements
        self.closePB = self.closePushButton

        # Signals
        self.closePB.clicked.connect(self.closeDialog)

    # Slots
    # Sulje button closes the dialog
    def closeDialog(self):
        self.close()


# Tests
if __name__ == "__main__":
    # Create a testing application
    testApp = QApplication(sys.argv)

    # Create a main window for testing a dialog
    testMainWindow = DialogTestMainWindow()
    testMainWindow.show()

    # Run the testing application
    testApp.exec()