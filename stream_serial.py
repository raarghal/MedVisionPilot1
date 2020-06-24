import time
import serial


ser = serial.Serial( port = '/dev/ttyUSB0', baudrate=9600, parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=1)

#ser = serial.Serial('/dev/ttyUSB0', 9600, 7, 'E', 2, timeout=1) 

while 1:
	ser.write(b'W\r')	
	x = ser.readline()
	print(x)




