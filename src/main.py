from serial_connection import SerialConnection
from network_connection import NetworkServer, NetworkClient

class Main:
	"""A class for establishing connections"""
	
	def start_serial_conn(self, port): 
		self.serial_conn = SerialConnection(port)
		self.serial_conn.open()
		self.serial_conn.flush_input()
		self.serial_conn.read()

	def stop_serial_conn(self):
		self.serial_conn.flush_input()
		self.serial_conn.close()

main = Main()
#main.start_serial_conn('/dev/ttyUSB0')

