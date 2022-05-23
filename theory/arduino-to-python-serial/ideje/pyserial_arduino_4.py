# -*- coding: utf-8 -*-
"""
  example for sending potentimeter value to PC over serial
  and testing python code
3rd EXAMPLE IS SO WE CAN PUT CODE IN ORDER IN AN ARHITECTURE AND FUNCTION
  
CLOSE TO AUTOMATING ARDUINO SERIAL MONITOR
"""

import serial
import time

from serial.tools import list_ports

#---------------------SERIAL PORT FUNCTIONS-------------------------------
def get_ports():
    """
    get a list of all active ports on PC

    Returns
    -------
    ports : list of ports
        DESCRIPTION.

    """
    ports = serial.tools.list_ports.comports()

    #number of COM ports on computer
    print("total COM ports = " + str(len(ports))) 

    return ports

def findArduino(portsFound):
    #initialize variables
    commPort='none'
    numConnections = len(portsFound)

    for i in range(0,numConnections):
        port = portsFound[i]
        strPort = str(port)

    if numConnections == 0:
        strPort = ""

    #search string in port names and split it
    """
    DEFAULT STRING NAME OF ARDUINO PORT
    COM3 - Arduino Uno
    we split by spaces
    list[]=[COM3,-,Arduino,Uno]
    list[0] = COM3
    """

    if 'Arduino' in strPort:
        splitPort = strPort.split(' ')
        commPort = (splitPort[0])
        print("Arduino found on " + str(splitPort[0]))
    else:
        commPort = ""
        print("Arduino not found")
    return commPort

def init_serial():
    global port
    
    port = serial.Serial(
        "COM5",
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
    )
    
    # wait for connection to be established
    time.sleep(2)

    port.flush()
    port.flushInput()
    port.flushOutput()
    print("Port is open")
   
def read_serial():
    """
    Če med branjem pride do prekinitve povezave javi to napako:
    SerialException: ClearCommError failed 
    (PermissionError(13, 'The device does not recognize the command.', None, 22))

    Returns
    -------
    rx_string : TYPE
        DESCRIPTION.

    """
    global port
 
    rx_string_n = port.readline().decode('ascii') #RESULT = 453
    
    rx_string = rx_string_n.rstrip() 
    
    return rx_string


def close_serial():
    """
    Returns
    -------
    None.

    """
    global port
    
    port.flush()
    port.flushInput()
    port.flushOutput()
    port.close()
    print("Port is closed")


def main():
    
    # get a list of all available COM serial ports
    portsFound = get_ports()
    print(portsFound)
    
    # check if any of ports found is and Arduino port
    arduino_port = findArduino(portsFound)
    print(arduino_port)
    
    # if arduino_port is an empty string "", than quit program
    if arduino_port != "":
        arduino_connected = True        
    else:
        arduino_connected = False
    print(arduino_connected)

    if arduino_connected:
        init_serial()
            
        try:
            while True:
                rx_data = read_serial()
                print(rx_data)
                time.sleep(0.09)            # wait (sleep) 0.1 seconds
        
        except KeyboardInterrupt:
            print('KeyboardInterrupt!')
            close_serial()

        except serial.SerialException:
            print('napaka komunikacije!')
            #close_serial()
            
        except:
            print("An exception occurred")
            close_serial()

if __name__ == "__main__":
    # execute only if run as a script
    print(' ctr + c = exit\n')
    time.sleep(1)
    main()
    print('program se je zaustavil')