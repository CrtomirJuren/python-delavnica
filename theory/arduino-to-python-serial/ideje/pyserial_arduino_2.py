# -*- coding: utf-8 -*-
"""
 2ND EXAMPLE IS SO WE CAN PUT CODE IN ORDER IN AN ARHITECTURE AND FUNCTION
  
CLOSE TO AUTOMATING ARDUINO SERIAL MONITOR
"""

import serial
import time

def init_serial():
    global port
    print("Opening port")
    
    port = serial.Serial(
        "COM16",
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
   
def read_serial():
    print("Reading data")

    global port
 
    rx_string_n = port.readline().decode('ascii') #RESULT = 453
    
    rx_string = rx_string_n.rstrip() 
    
    return rx_string


def close_serial():
    global port
    
    print("Closing port")
    port.flush()
    port.flushInput()
    port.flushOutput()
    port.close()


def main():
    init_serial()
        
    try:
        # while True:
        while True:
            rx_data = read_serial()
            print(rx_data)
            time.sleep(0.09)            # wait (sleep) 0.1 seconds
    
    except KeyboardInterrupt:
        print('KeyboardInterrupt!')
        close_serial()
    
    except:
        print("An exception occurred")
        close_serial()
   
if __name__ == "__main__":
    # execute only if run as a script
    print(' ctr + c = exit\n')
    time.sleep(1)
    main()