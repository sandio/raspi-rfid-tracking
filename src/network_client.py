import socket
from time import sleep
from serial_connection import SerialConnection

class NetworkClient:
	"""A class for sending readings to a server"""

	def __init__(self):
		# Create an INET, STREAMing socket
		self.cli_sock = socket.socket(
			socket.AF_INET, socket.SOCK_STREAM)
		# Connect to a remote  socket at host and port
		self.cli_sock.connect(('pi2' , 1234))
		
		self.serial_conn = SerialConnection('/dev/ttyUSB0', 30)
		self.serial_conn.open()
		self.serial_conn.flush_input()
	
	def send(self):
		try:
			while True:
				data = self.serial_conn.read()
				self.cli_sock.send(data)
		except KeyboardInterrupt:
			self.serial_conn.close()
			self.cli_sock.close()

net_cli = NetworkClient()
net_cli.send()
