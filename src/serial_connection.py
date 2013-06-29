from time import sleep
import serial

class SerialConnection:

	def __init__(self, port, timeout):
		self.ser = serial.Serial()
		self.ser.port = port
		self.ser.timeout = timeout
	
	def open(self):
		self.ser.open()
		return self.ser.isOpen()

	def close(self):
		self.ser.close()
		return self.ser.isOpen()

	def flush_input(self):
		while self.ser.inWaiting() > 14:
			self.ser.flushInput()
			sleep(0.3)
			print self.ser.inWaiting()
	
	def read(self):
		buf = ''
		while not ' ' in buf:
			buf += self.ser.read()
		return buf
