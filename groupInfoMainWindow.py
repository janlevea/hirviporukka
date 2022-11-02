# APPLICATION FOR SHOWING SUMMARY DATA ABOUT MEAT GIVEN TO SHARE GROUP
# ====================================================================

# LIBRARIES AND MODULES
# ---------------------

import sys # Needed for starting the application
import psycopg2
from PyQt5.QtWidgets import * # All widgets
from PyQt5.uic import loadUi
import ui_groupInfoMainWindow

# CLASS DEFINITIONS FOR THE APP
# -----------------------------
class GroupMainWindow(QMainWindow):
    # Constructor, a method for creating objects from this class
    def __init__(self):
        QMainWindow.__init__(self)
    
        # Create an UI from the ui file
        loadUi("groupInfoMainWindow.ui", self)

    