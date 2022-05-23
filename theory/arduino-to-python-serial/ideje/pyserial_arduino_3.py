# -*- coding: utf-8 -*-
"""
 2ND EXAMPLE IS SO WE CAN PUT CODE IN ORDER IN AN ARHITECTURE AND FUNCTION
  
CLOSE TO AUTOMATING ARDUINO SERIAL MONITOR
"""

import serial
import time
from datetime import datetime
from pathlib import Path

# spremeni v univerzalni desktop
DESKTOP_PATH = Path.home() / 'Desktop'
outfile = DESKTOP_PATH / 'test.txt'
port = ''

def init_serial():
    global port
    
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
    print("Port is open")
   
def read_serial():
    global port
 
    rx_string_n = port.readline().decode('ascii') #RESULT = 453
    
    rx_string = rx_string_n.rstrip() 
    
    return rx_string

def close_serial():
    global port
    
    port.flush()
    port.flushInput()
    port.flushOutput()
    port.close()
    print("Port is closed")

def get_time():
    t = datetime.now()
    s = t.strftime('%Y-%m-%d %H:%M:%S.%f')
    return s[:-3]

def main():
    init_serial()
        
    try:
        with open(outfile,'w') as f:
            # write header
            f.write("sample"+'\t'+"sensor"+'\n')
            sample = 0

            while True: # while loop that loops forever
                while (port.inWaiting()==0): #Wait here until there is data
                    pass #do nothing

                # time dd/mm/YY H:M:S
                now = get_time()
                rx_data = read_serial()
                print(sample, "   " , rx_data)
                f.write(str(sample)+'\t'+str(rx_data) + '\n')
                f.flush()

                # increment sample number
                sample += 1

    except KeyboardInterrupt:
        print('KeyboardInterrupt!')
        close_serial()
    
    except Exception as e :
        print("An exception occurred", e)
        close_serial()
   
    
if __name__ == "__main__":
    # execute only if run as a script
    print(' ctr + c = exit\n')
    time.sleep(1)
    main()