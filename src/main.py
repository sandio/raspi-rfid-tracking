from serial_connection import SerialConnection

class Main:
	"""A class for establishing connections"""
	
	def start_serial_conn(self, port, timeout): 
		self.serial_conn = SerialConnection(port, timeout)
		self.serial_conn.open()
		self.serial_conn.flush_input()
	
	def read_serial_data(self):
		while True:
			print self.serial_conn.read()

	def stop_serial_conn(self):
		self.serial_conn.flush_input()
		self.serial_conn.close()

main = Main()
main.start_serial_conn('/dev/ttyUSB0', 30)
main.read_serial_data()
