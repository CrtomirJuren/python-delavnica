"""


"""
# --- imports ---
import sys
from datetime import datetime
import logging

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
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
win_W = 500
win_H = 300
res_WH = res_W // 2
res_HH = res_H // 2
win_pos_W = res_WH - (win_W // 2)
win_pos_H = res_HH - (win_H // 2)

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.setGeometry(win_pos_W, win_pos_H, win_W, win_H)
        self.setWindowTitle("Application")

        # set user interface stuff
        self.UI()

    def UI(self):
        # -----------------------------
        # --- create buttons layout ---
        # -----------------------------
        # self.button_widgets = QWidget()
        self.button_widgets = QWidget()
        button_layout = QHBoxLayout(self.button_widgets)

        # --- create buttons ---
        # --- button EXIT ---
        btnExitApp = QPushButton("Exit App")
        btnExitApp.clicked.connect(self.exit_app_event)     # connect signal to slot
        btnExitApp.setStyleSheet("background-color : pink") # color of button
        
        # --- button START ---
        btnStart=QPushButton("Start",self)
        btnStart.clicked.connect(self.start_btn_event)

        # --- button pause unpause ---
        btnPauseUnpause=QPushButton("Pause",self)
        btnPauseUnpause.clicked.connect(self.pause_unpause_btn_event)

        # --- button STOP ---
        btnStop=QPushButton("Stop",self)
        btnStop.clicked.connect(self.stop_btn_event)

        # --- add buttons to button layout---
        button_layout.addWidget(btnStart)
        button_layout.addWidget(btnPauseUnpause)
        button_layout.addWidget(btnStop)
        button_layout.addWidget(btnExitApp)

        # -----------------------------
        # --- create labels layout ---
        # -----------------------------
        # self.display_widgets = QWidget()
        # display_layout = QHBoxLayout(self.display_widgets)
        # # --- create label ---
        # self.lbl_time_display = QLabel("00:00:00", self)
        # # resizing the widget

        # # self.lbl_time_display.set

        # --- add buttons to button layout---
        # button_layout.addWidget(lbl_time_display)

        # ---------------------------
        # --- main central layout ---
        # ---------------------------
        self.central_widget = QWidget()
        # create central layout
        central_layout = QVBoxLayout(self.central_widget)
        # add other layouts to central layout
        # central_layout.addWidget(self.display_widgets)
        central_layout.addWidget(self.button_widgets)
        # Set the layout on the application's window
        self.setCentralWidget(self.central_widget)

        # --------------------
        # --- show widgets ---
        # --------------------
        self.show()

    # -------------------------------------
    # --- GUI functions called by timer ---
    # -------------------------------------
    def updateClock_timer_event(self):
        logger.debug('clock update timer event')

    # ---------------------------------------
    # --- GUI functions called by buttons ---
    # ---------------------------------------
    # slot
    def exit_app_event(self):
        logger.debug('exit_app_event')
        # close application
        self.close()

    def start_btn_event(self):
        logger.debug('start btn pressed')

    def stop_btn_event(self):
        logger.debug('stop btn pressed')

    def pause_unpause_btn_event(self):
        logger.debug('pause unpause btn pressed')

def window():
    # --- start GUI ---
    logger.debug('Application started')
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_()) # clean app exit

if __name__ == '__main__':
    window()