""" install py-serial

conda install -c anaconda pyserial
"""
#------------------------------------------------------------------
#------------------------------------------------------------------
#------------------------------------------------------------------
import serial
import time

# --- 1. start komunikacije ---
# open and reserve serial port
ser = serial.Serial('COM16', 9600)

# clear ports
ser.flushInput()
ser.flushOutput()

# wait for connection to be established
time.sleep(2)

# --- 2. read data ---
# read a byte string
rx_byte = ser.readline()         

# decode byte string into Unicode 
rx_string_n = rx_byte.decode()   

# remove \n and \r
rx_string = rx_string_n.rstrip() 

# convert string to float
analog_data = float(rx_string)        

# print received data
print('--- rx_byte ---')
print(rx_byte)
print('--- rx_string_n ---')
print(rx_string_n)
print('--- rx_string ---')
print(rx_string)
print('--- analog_data ---')
print(analog_data)

# --- 3. stop communication ---
ser.close()    

# 1. start komunikacije
# 2. preberi podatke
# 3. stop komunikacije