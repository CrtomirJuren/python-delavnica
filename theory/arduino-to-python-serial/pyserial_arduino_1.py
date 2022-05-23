""" install py-serial

conda install -c anaconda pyserial

"""
#------------------------------------------------------------------
#------------------------------------------------------------------
#------------------------------------------------------------------
import serial
import time
import matplotlib.pyplot as plt

# --- initialization ---
# open and reserve serial port
ser = serial.Serial('COM16', 9600)

# clear ports
ser.flushInput()
ser.flushOutput()

# wait for connection to be established
time.sleep(2)

# --- receive data and save it to array ---
# Read and record the data
data =[]                       # empty list to store the data
for i in range(50):

    # wait until data is received in rx buffer
    while not ser.in_waiting:
        time.sleep(0.01)

    # read a byte string
    rx_byte = ser.readline()  

    # decode byte string into Unicode 
    rx_string_n = rx_byte.decode()
    
    # remove \n and \r
    rx_string = rx_string_n.rstrip() 

    if rx_string != '':
        value = float(rx_string)
        data.append(value)
        print(value)

# --- close port ---
ser.close()    

# --- print results ---
# print(data)

plt.plot(data)
plt.show()
