from time import sleep
import serial

class SerialConnection:

	def __init__(self, port):
		self.ser = serial.Serial()
		self.ser.port = port
	
	def open_port(self):
		self.ser.open()
		return self.ser.isOpen()

	def close_port(self):
		self.ser.close()
		return self.ser.isOpen()

	def flush_input(self):
		while self.ser.inWaiting() > 14:
			self.ser.flushInput()
			sleep(0.4)
			print self.ser.inWaiting()
	
	def read_data(self):
		try:
			buf = ''
			while True:
				char = self.ser.read()
				if char != ' ':
					buf += char
				else:
					print buf
					buf = ''
		except KeyboardInterrupt:
			self.close_port()