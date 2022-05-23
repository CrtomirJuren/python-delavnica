import sys, os
import logging
from pathlib import Path
import pyqtgraph as pg #conda install -c anaconda pyqtgraph
import numpy as np
# from sqlalchemy import true
from numpy_ringbuffer import RingBuffer #pip install numpy_ringbuffer
import random

from PyQt5.QtCore import QTimer
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QApplication, 
                            QPushButton,
                            QMainWindow,
                            QWidget,
                            QHBoxLayout,
                            QVBoxLayout,)

# create logger for debugging
logger = logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format ='%(message)s')

# Screen resolution
res_W = 1920
res_H = 1080
win_W = 800
win_H = 500

# constants for center of screen
res_WH = res_W // 2
res_HH = res_H // 2
win_pos_W = res_WH - (win_W // 2)
win_pos_H = res_HH - (win_H // 2)

N_SAMPLES = 1000
SAMPLE_RATE = 100

class MainWindow(QMainWindow):
    """ 
    When creating instance of class, we pass it a window reference.
    This becomes win -> self. Can be confusing.
    Transforms:
    win.setWindowTitle("") --> self.setWindowTitle("")
    QtWidgets.QLabel(win) --> QtWidgets.QLabel(self)
    """
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.setGeometry(win_pos_W, win_pos_H, win_W, win_H)
        self.setWindowTitle("Arduino Data Acquisition")
        self.initUI()

        # initialize fixed X POINTS graph data
        self.x_data = np.arange(0, N_SAMPLES/SAMPLE_RATE, 1/SAMPLE_RATE, dtype=np.single)
        # initialize buffer for Y POINTS graph data
        self.y_data = RingBuffer(capacity = N_SAMPLES, dtype=np.single)

        # initialize buffer with values
        for i in range(N_SAMPLES):
            self.y_data.append(np.NaN)

        # create timer for arduino DAQ
        self.timer_data_update = QTimer()
        self.timer_data_update.timeout.connect(self.read_data_event)
        self.timer_data_update.start(10) #ms

        # create timer for plot update
        self.timer_plot_update = QTimer()
        self.timer_plot_update.timeout.connect(self.update_plot_event)
        self.timer_plot_update.start(33) #ms

        self.isDaqRunning = False

    def initUI(self):
        # --------------------------------------
        # --- create buttons widget - layout ---
        # create buttons layout
        self.button_widgets = QWidget()
        button_layout = QHBoxLayout(self.button_widgets)

        # --- button START ---
        b1 = QPushButton("Start",self.button_widgets)
        b1.clicked.connect(self.start_daq_event) # connect signal to slot

        # --- button STOP ---
        b2 = QPushButton("Stop")
        b2.clicked.connect(self.stop_daq_event) # connect signal to slot

        # --- button SAVE ---
        b3 = QPushButton("Save Data")
        b3.clicked.connect(self.save_data_event) # connect signal to slot

        # --- button EXIT ---
        b4 = QPushButton("Exit App")
        b4.clicked.connect(self.exit_app_event) # connect signal to slot
        # changing color of button
        b4.setStyleSheet("background-color : pink")

        # add buttons to button layout
        button_layout.addWidget(b1)
        button_layout.addWidget(b2)
        button_layout.addWidget(b3)
        button_layout.addWidget(b4)
        
        # -----------------------------------
        # --- create plot widget - layout ---
        self.plot_widget = pg.PlotWidget()
        self.plot = self.plot_widget.plot([0],[0])
        # self.plot_widget.setRange(xRange=[0,1000])
        self.plot_widget.setRange(yRange=[0,10])

        # ---------------------------
        # --- main central layout ---
        self.central_widget = QWidget()

        # create centarl layout
        central_layout = QVBoxLayout(self.central_widget)

        # add other widgets-layouts to central layout
        central_layout.addWidget(self.plot_widget)
        central_layout.addWidget(self.button_widgets)

        # Set the layout on the application's window
        self.setCentralWidget(self.central_widget)

    # slot
    def start_daq_event(self):
        logger.debug('start_scan_event')
        
        # set flag for data acquisition        
        self.isDaqRunning = True

        # clear data buffer
        for i in range(N_SAMPLES):
            self.y_data.append(np.NaN)

    # slot
    def exit_app_event(self):
        logger.debug('exit_app_event')

        # close application
        self.close()

    # slot
    def save_data_event(self):
        logger.debug('save_data_event')

    # slot
    def stop_daq_event(self):
        logger.debug('stop_scan_event')

        # clear flag for data acquisition        
        self.isDaqRunning = False

    # slot
    def read_data_event(self):
        # only update points if data is running
        if self.isDaqRunning:
            data_point = random.random()

            self.y_data.append(data_point)

    # slot
    def update_plot_event(self):
        self.plot.setData(self.x_data,
                          self.y_data)


def window():
    # --- start GUI ---
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_()) # clean app exit

if __name__ == '__main__':
    window()









