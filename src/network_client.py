import socket
from time import sleep

class NetworkClient:
	"""A class for sending readings to a server"""

	def __init__(self):
		# Create an INET, STREAMing socket
		self.cli_sock = socket.socket(
			socket.AF_INET, socket.SOCK_STREAM)
		# Connect to a remote  socket at host and port
		self.cli_sock.connect((socket.gethostname(), 1234))
		self.alive = True
	
	def send(self):
		try:
			while self.alive:
				self.cli_sock.send('Sending from client')
				sleep(1)
		except KeyboardInterrupt:
			self.alive = False
			self.cli_sock.close()

net_cli = NetworkClient()
net_cli.send()
