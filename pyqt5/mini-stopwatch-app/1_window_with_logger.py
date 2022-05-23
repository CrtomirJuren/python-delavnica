"""
- added logger library for debugging all events.
- this is necessary so we we can debug if app working correctly. Freezing etc...
"""
# --- imports ---
import sys
from datetime import datetime
import logging

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont,QCloseEvent
from PyQt5.QtCore import QTimer

# --- logger ---
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)     # DEBUG shows all messages
date_strftime_format = "%H:%M:%S" # set logger print formatting
message_format = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(format= message_format, datefmt= date_strftime_format, stream=sys.stdout)

# --- Screen resolution and position ---
res_W = 1920
res_H = 1080
win_W = 800
win_H = 500
res_WH = res_W // 2
res_HH = res_H // 2
win_pos_W = res_WH - (win_W // 2)
win_pos_H = res_HH - (win_H // 2)

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        # set window title
        self.setWindowTitle("Application")
        # set window position and size
        self.setGeometry(win_pos_W, win_pos_H, win_W, win_H)
        # set user interface stuff
        self.UI()

    # -------------------------------------
    # --- GUI button, widgets ---
    # -------------------------------------
    def UI(self):
        self.show()

    # -------------------------------------
    # --- GUI functions called by timer ---
    # -------------------------------------

    # ---------------------------------------
    # --- GUI functions called by buttons ---
    # ---------------------------------------

def window():
    # --- start GUI ---
    logger.debug('Application started')
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_()) # clean app exit

if __name__ == '__main__':
    window()