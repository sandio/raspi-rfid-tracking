import serial

ser = serial.Serial('/dev/ttyUSB0', timeout=10)
print ser.name
print ser.isOpen()
while(1):
	print ser.read(7).strip()
