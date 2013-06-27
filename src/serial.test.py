from time import sleep
import serial

ser = serial.Serial('/dev/ttyS0', timeout=10)
print ser.name
print ser.isOpen()
ser.flushInput()
sleep(20)
print ser.inWaiting()
#print ser.read(ser.inWaiting())
while True:
	print ser.read(7)
