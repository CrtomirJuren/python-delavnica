"""
- minimal code for pyqt main application window with size and position
"""
# --- imports ---
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer

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
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_()) # clean app exit

if __name__ == '__main__':
    window()