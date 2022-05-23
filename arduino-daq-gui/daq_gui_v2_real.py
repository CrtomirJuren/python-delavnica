""" 
REQUIREMENTS:
- pyserial: conda install -c anaconda pyserial
- tqdm
- numpy_ringbuffer: pip install numpy_ringbuffer
- pyqtgraph: conda install -c anaconda pyqtgraph
"""
import sys, os
import logging
from pathlib import Path
import pyqtgraph as pg #conda install -c anaconda pyqtgraph
import numpy as np
from numpy_ringbuffer import RingBuffer #pip install numpy_ringbuffer
import random
from time import sleep
from datetime import datetime
import serial
from serial.tools import list_ports
import pandas as pd

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
win_W = 1200
win_H = 500
res_WH = res_W // 2
res_HH = res_H // 2
win_pos_W = res_WH - (win_W // 2)
win_pos_H = res_HH - (win_H // 2)

# sample rates for data acquisition
N_SAMPLES = 1000    # buffer length
SAMPLE_RATE = 100   # acquisition speed from arduino

# initialize logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)     # DEBUG shows all messages
date_strftime_format = "%H:%M:%S" # set logger print formatting
message_format = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(format= message_format, datefmt= date_strftime_format, stream=sys.stdout)

# GUI
class MainWindow(QMainWindow):
    """ 
    """
    # --------------------------------------
    # --- GUI main object initialization ---
    # --------------------------------------
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.setGeometry(win_pos_W, win_pos_H, win_W, win_H)
        self.setWindowTitle("Arduino Data Acquisition")

        # ---
        self.init_ui()

        self.init_paths()

        self.init_data_buffer()

        self.init_arduino_com()

        self.start_arduino_com(self.arduino_port)
        # ---

        # create timer for arduino DAQ
        self.timer_data_update = QTimer()
        self.timer_data_update.timeout.connect(self.read_data_event)
        self.timer_data_update.start(8) #ms

        # create timer for plot update
        self.timer_plot_update = QTimer()
        self.timer_plot_update.timeout.connect(self.update_plot_event)
        self.timer_plot_update.start(50) #ms

        self.isDaqRunning = False

    # --------------------------------
    # --- initialization functions ---
    # --------------------------------
    def init_ui(self):
        # --------------------------------------
        # --- create buttons widget - layout ---
        # --------------------------------------    
        # create buttons layout
        self.button_widgets = QWidget()
        button_layout = QHBoxLayout(self.button_widgets)

        # --- button START ---
        b1 = QPushButton("Start / Clear",self.button_widgets)
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
        # -----------------------------------
        
        self.plot_widget = pg.PlotWidget()
        self.plot = self.plot_widget.plot([0],[0])
        self.plot_widget.setRange(yRange=[400,1000])

        # ---------------------------
        # --- main central layout ---
        # ---------------------------

        self.central_widget = QWidget()

        # create centarl layout
        central_layout = QVBoxLayout(self.central_widget)

        # add other widgets-layouts to central layout
        central_layout.addWidget(self.plot_widget)
        central_layout.addWidget(self.button_widgets)

        # Set the layout on the application's window
        self.setCentralWidget(self.central_widget)

    def init_data_buffer(self):
         # initialize fixed X POINTS graph data
        self.x_data = np.arange(0, N_SAMPLES/SAMPLE_RATE, 1/SAMPLE_RATE, dtype=np.single)
        # initialize buffer for Y POINTS graph data
        self.y_data = RingBuffer(capacity = N_SAMPLES, dtype=np.single)

        # initialize buffer with values
        for i in range(N_SAMPLES):
            self.y_data.append(np.nan)

    def init_paths(self):
        # this script folder path
        self.script_dir = Path( __file__ ).parent.absolute()
        # path for saving files
        self.log_dir = self.script_dir / 'logs'     

    # ---------------------------------------
    # --- GUI functions called by buttons ---
    # ---------------------------------------

    # slot 
    def start_daq_event(self):
        logger.debug('start_daq_event')
       
        # set flag for data acquisition        
        self.isDaqRunning = True

        # clear data buffer
        for i in range(N_SAMPLES):
            self.y_data.append(np.nan)

        # before start clear usb input bufffer
        self.clear_rx_buffer()

    # slot
    def exit_app_event(self):
        logger.debug('exit_app_event')
        
        self.stop_arduino_com()

        # close application
        self.close()

    # slot
    def save_data_event(self):
        logger.debug('save_data_event')
        
        self.save_measurement_to_excel()

    # slot
    def stop_daq_event(self):
        logger.debug('stop_scan_event')

        # clear flag for data acquisition        
        self.isDaqRunning = False

    # -----------------------------------------
    # --- GUI functions called periodically ---
    # -----------------------------------------
    # slot callded by Timer 
    def read_data_event(self):

        # only update points if data is running
        if self.isDaqRunning:           
            # read data if in buffer
            while self.ser.in_waiting:
                # read single rx line from rx serial buffer
                rx_data_str = self.read_single_rx_line()
                
                # if rx_data is ok, add to data
                if rx_data_str != None:
                    # arduino is sending data in mV
                    mili_volts = float(rx_data_str)
                    # add arduino data to buffer    
                    self.y_data.append(mili_volts)

    # slot callded by Timer 
    def update_plot_event(self):
        self.plot.setData(self.x_data,
                          self.y_data)

    # ---------------------------------------
    # --- arduino communication functions ---
    # ---------------------------------------
    def get_ports(self):
        """
        get a list of all active SERIAL COM ports on PC
        """   
        ports = serial.tools.list_ports.comports()

        return ports

    def search_arduino(self, com_ports):
        #initialize variables
        arduino_port = None
        num_com_ports = len(com_ports)

        # only check if not empty com port array
        if num_com_ports != 0:
            # check ports until one with Arduino is found
            for port in com_ports:
                # convert <class 'serial.tools.list_ports_common.ListPortInfo'> to string
                port_name = str(port)

                #search string in port names and split it
                # COM3 - Arduino Uno
                # port_name_split = [COM3,-,Arduino,Uno]
                # list[0] = COM3
                port_name_split = port_name.split(' ')
                if 'Arduino' in port_name_split:
                    arduino_port = port_name_split[0]
                    # exit for loop
                    break

        return arduino_port
    
    def clear_rx_buffer(self):
        # clear serial USB buffer of data before start of acquisition
        # because we are receiving data from when communication is opened
        self.ser.reset_input_buffer()

    def read_single_rx_line(self):
        # read a byte string
        rx_byte = self.ser.readline()  
        # decode byte string into Unicode 
        rx_string_n = rx_byte.decode()
        # remove \n and \r
        rx_string = rx_string_n.rstrip() 

        # If empty string, bad data
        if rx_string == '':
            return None
        # if data is good, transform to number value
        else:  
            return rx_string

    def init_arduino_com(self):
        # 1.) get current COM ports
        logger.info("Searching for COM ports")
        com_ports = self.get_ports()
        logger.info(f'Found {len(com_ports)} COM ports')

        # 2.) check if any port is Arduino
        logger.info("Searching for Arduino")
        self.arduino_port = self.search_arduino(com_ports)
        if self.arduino_port is not None:
            logger.info(f'Arduino found on {self.arduino_port}')
        else:
            logger.info("Arduino not found")

        # 3.) start communication with arduino
        logger.info("Opening communication")    

    def start_arduino_com(self, arduino_port):
        # open and reserve serial port
        # ser = serial.Serial(arduino_port, 9600)
        self.ser = serial.Serial(arduino_port, 115200)

        # wait for com to be opened
        while not self.ser.is_open:
            sleep(0.1)

    def stop_arduino_com(self):
        self.ser.flush()
        self.ser.close()

    # -----------------------
    # --- other functions ---
    # -----------------------
    def save_measurement_to_excel(self):
        logger.debug('saving data to excel')
        # stack two 1-D arrays into 2-D arrays
        meas_data = np.column_stack((self.x_data, np.array(self.y_data)))

        measurement_name = 'test'
        # build timestamp
        timestamp = datetime.now().strftime("%Y_%m_%d-%H_%M_%S")
        # build filename with timestamp
        filename = timestamp + '_' + measurement_name

        # build filepath
        filepath = self.log_dir / (filename + '.xlsx')
        # if folder log dir doesnt exist create it
        Path(self.log_dir).mkdir(parents=True, exist_ok=True)

        column_names = ['time[s]', 'voltage[mV]']
        
        # transform numpy array to pandas dataframe
        # vrstico dodamo zadnjim podatkom
        dataframe = pd.DataFrame(meas_data, columns = column_names)
        # pandas dataframe to excel
        dataframe.to_excel(filepath, index=False)

        logger.debug('saving data done')

def window():
    # --- start GUI ---
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_()) # clean app exit

if __name__ == '__main__':
    window()









