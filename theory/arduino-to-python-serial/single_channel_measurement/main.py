""" 

REQUIREMENTS:
- pyserial
- tqdm

conda install -c anaconda pyserial

"""
# --- imports ---
import sys
from time import sleep
from datetime import datetime
from pathlib import Path
# from tqdm import tqdm # for progress bar
from tqdm import trange # for progress bar
import logging # library for advanced print

import serial
from serial.tools import list_ports

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

# --- global variables ---
global ser

# --- logging info library ---
# create logger object
logger = logging.getLogger(__name__)

# set logger level
# logger.setLevel(logging.CRITICAL) # only shows critical
# logger.setLevel(logging.WARNING)  # doesnt show debug, info
# logger.setLevel(logging.INFO)     # doesnt show debug
logger.setLevel(logging.DEBUG)     # shows all messages

# set logger print formatting
date_strftime_format = "%H:%M:%S"
message_format = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(format= message_format, datefmt= date_strftime_format, stream=sys.stdout)

# --- functions ---
def get_ports():
    """
    get a list of all active SERIAL COM ports on PC
    Returns
    -------
    ports : list of ports
        DESCRIPTION.
    """   
    ports = serial.tools.list_ports.comports()

    #number of COM ports on computer
    # print("Number of COM ports = " + str(len(ports))) 

    return ports

def search_arduino(com_ports):
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

def start_communication(arduino_port):
    global ser 

    # open and reserve serial port
    # ser = serial.Serial(arduino_port, 9600)
    ser = serial.Serial(arduino_port, 9600)

    # wait for com to be opened
    while not ser.is_open:
        sleep(0.1)

def read_single_rx_line():
    global ser 

    # read a byte string
    rx_byte = ser.readline()  
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

def stop_communication():
    global ser 

    # ser.flush()
    ser.flushInput()
    ser.flushOutput()
    ser.close()

def graph_measurement(meas_data):
# podatke transponiramo, da lažje dostopamo do stolpcev
    t_arr = meas_data.T[0]  
    s_arr = meas_data.T[1]  

    # graf poti
    # IZRIŠEMO PODATKE
    fig, ax = plt.subplots()

    ax.plot(t_arr, s_arr)
    ax.set_title(meas_name)
    ax.set_ylabel('U [Volt]')
    ax.set_xlabel('t [second]')
    ax.grid()

    plt.tight_layout()
    plt.show()

def save_measurement_to_excel(meas_data, measurement_name):
    # build timestamp
    timestamp = datetime.now().strftime("%Y_%m_%d-%H_%M_%S")

    # build filename with timestamp
    filename = timestamp + '_' + measurement_name

    # build filepath
    filepath = log_dir / (filename + '.xlsx')
    print('Saving measurement to file: ', filepath)

    column_names = ['time[s]', 'voltage[V]']
    # transform numpy array to pandas dataframe
    dataframe = pd.DataFrame(meas_data, columns = column_names)
    # dataframe = pd.DataFrame(meas_data)
    # pandas dataframe to excel
    dataframe.to_excel(filepath, index=False)

if __name__ == '__main__':

    # 0.) paths
    # this script folder path
    script_dir = Path( __file__ ).parent.absolute()
    log_dir = script_dir / 'logs'     # path for saving files
    logger.debug(script_dir)
    logger.debug(log_dir)

    # 1.) user measurement configuration
    meas_duration_sec = 10
    meas_name = 'meritev_napetosti'
    graph_data = True
    save_graph_to_file = True
    save_data_to_excel = True

    # 1.) get current COM ports
    logger.info("Searching for COM ports")
    com_ports = get_ports()
    logger.info(f'Found {len(com_ports)} COM ports')

    # 2.) check if any port is Arduino
    logger.info("Searching for Arduino")
    arduino_port = search_arduino(com_ports)
    if arduino_port is not None:
        logger.info(f'Arduino found on {arduino_port}')
    else:
        logger.info("Arduino not found")

    # 3.) start communication with arduino
    logger.info("Opening communication")    
    start_communication(arduino_port)

    # 4.) read multiple samples of serial data
    logger.info("Reading data and storing it to buffer")
    
    # 4.1) rezervacija praznega arraya stolpcev = time + N_signals
    meas_data= np.empty((0, 2))   
    
    # start data acquisition
    # arduino sampling -> 10 samples per second
    N_samples = meas_duration_sec * 10 + 1 # +1., zato ker pyton upošteva od 0 do 9.9, da bo od 0 do 10
    progress_bar = trange(N_samples, leave=True)

    # clear serial USB buffer of data before start of acquisition
    # because we are receiving data from when communication is opened
    ser.reset_input_buffer()

    for i in progress_bar:
        t = i * 0.1    # 1 sample = 100 ms
        
        # wait until data is received into serial buffer
        while not ser.in_waiting:
            sleep(0.02)
        
        # read single rx line from rx serial buffer
        rx_data_str = read_single_rx_line()
        
        # if rx_data is ok, add to data
        if rx_data_str != None:
            # arduino is sending data in mV
            mili_volts = float(rx_data_str)
            # convert milivolts to volts
            volts = mili_volts / 1000
            # create numpy array to add to buffer
            row = np.array([t, volts])
            # vrstico dodamo zadnjim podatkom
            meas_data = np.vstack((meas_data, row))
            # print current readed value
            # logger.debug(rx_data_v)

        # Adds text before progess bar
        progress_bar.set_description(f"t = {t:.1f} s U = {volts:.1f} V")  

    # 5.) ustavi komunikacijo
    logger.info("Closing communication")
    stop_communication()

    # 6.) shrani podatke v datoteko
    if save_data_to_excel:
        logger.info("Saving to file")
        save_measurement_to_excel(meas_data, meas_name)

    # 7.) nariši podatke
    # nazadnje narišemo podatke, ker plt.show() ustavi kodo
    if graph_data:
        logger.info("Graphing measurement")
        graph_measurement(meas_data)

    logger.info("Measurement application finished")