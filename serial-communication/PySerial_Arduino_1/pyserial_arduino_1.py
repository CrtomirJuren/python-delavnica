# -*- coding: utf-8 -*-
"""
  example for sending potentimeter value to PC over serial
  and testing python code
  
  https://www.arduino.cc/en/Tutorial/BuiltInExamples/SerialCallResponseASCII
  
---------------arduino code------------------
const int potentiometer_pin = A0;
int analog_data = 0;
  
void setup() {
  Serial.begin(9600);
}

void loop() {
  analog_data = analogRead(potentiometer_pin);
  Serial.println(analog_data);  // IMPORTANT delimiter, escape sequence for data is line feed = new line "\n"
  delay(200);
}

"""

#------------------------------------------------------------------
#------------------------------------------------------------------
#------------------------------------------------------------------
"""1st example WORKING
import serial
import time

device = serial.Serial("COM5", baudrate = 9600, timeout = 1)

while 1:
    #arduinoData = ser.readline() #RESULT = b'453\r\n'

    arduinoData = device.readline().decode('ascii') #RESULT = 453

    print(arduinoData)
"""
#------------------------------------------------------------------
#------------------------------------------------------------------
#------------------------------------------------------------------

"""
import serial
import time

# open and reserve serial port
ser = serial.Serial('COM5', 9600)

ser.flushInput()
ser.flushOutput()

# wait for connection to be established
time.sleep(2)

# empty variable to store the data
#analog_data = 0                       

# read a byte string
rx_byte = ser.readline()         

# decode byte string into Unicode 
rx_string_n = rx_byte.decode()   

# remove \n and \r
rx_string = rx_string_n.rstrip() 

# convert string to float
analog_data = float(rx_string)        

print(rx_byte)
print(rx_string_n)
print(rx_string)
print(analog_data)

ser.close()    

# Read and record the data
data =[]                       # empty list to store the data
for i in range(50):
    b = ser.readline()         # read a byte string
    string_n = b.decode()  # decode byte string into Unicode  
    string = string_n.rstrip() # remove \n and \r
    flt = float(string)        # convert string to float
    print(flt)
    data.append(flt)           # add to the end of data list
    time.sleep(0.1)            # wait (sleep) 0.1 seconds

ser.close()
"""
import serial
import time

port = serial.Serial("COM5", baudrate = 9600, timeout = 1)

port.flushInput()
port.flushOutput()

# wait for connection to be established
time.sleep(3)

try:
    while True:
        #simple one line code
        #arduinoData =  arduinoData.decode('ascii') #RESULT = 453

        #arduinoData = port.readline().decode('ascii') #RESULT = 453
        rx_byte = port.readline()
        print(rx_byte) #b'1000\r\n'
        
        # What is the character encoding of Arduino's Serial messages?
        #decoded_utf = rx_byte.decode('utf-8')
        #decoded_unicode = rx_byte.decode('unicode')
        
        rx_string_n = rx_byte.decode('ascii')
        print(rx_string_n) #'1000'
        
        # remove \n and \r
        rx_string = rx_string_n.rstrip() 
        print(rx_string)
        
        sensor = 5* int(rx_string) / 1024
        print(sensor)
        
        time.sleep(0.09)            # wait (sleep) 0.1 seconds

except KeyboardInterrupt:
    print('KeyboardInterrupt!')
    port.close()
    print('port closed')

except:
    print("An exception occurred")
    port.close()
    print('port closed')
    
""" VPRAŠANJA
KAJ SE JE ZGODILO TUKAJ?
a = string * 5
print(string)
print(a)
155
155155155155155
"""