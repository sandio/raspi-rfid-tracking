import select
import socket
import threading

class NetworkServer:
	"""A class for receiving readings from the other Pis"""
	
	def __init__(self):
		# Create an INET, STREAMing socket
		self.srv_sock = socket.socket(
			socket.AF_INET, socket.SOCK_STREAM)
		# Bind the socket to a public host and port
		self.srv_sock.bind((socket.gethostname(), 1234))
		# Become a server socket and queque max 5
		self.srv_sock.listen(5)
	
	def receive(self):
		try:
			# A list of receive threads
			rcv_thrs = []
			# Names of the threads
			name = 0
			while True:
				# Accept connections from outside
				(cli_sock, addr) = self.srv_sock.accept()
				print 'Connection from', addr
				# Create a receive thread to handle this stream
				rcv_thr = RcvThread(cli_sock, name)
				rcv_thr.start()
				# Append this thread to the other receive threads
				rcv_thrs.append(rcv_thr)
				name += 1
		except KeyboardInterrupt:
			# Go through the list of theads
			for rcv_thr in rcv_thrs:
				# Stop a thread by exiting its receiving loop
				rcv_thr.stop()
				# Wait for the thread to terminate for 30s
				rcv_thr.join(30)
				# Check if the thread has terminated
				if rcv_thr.isAlive():
					print 'Thread', rcv_thr.get_name(), 'alive'
			# Close the server socket
			self.srv_sock.close()
		
class RcvThread(threading.Thread):
	"""A tread class that receives readings over the network"""

	def __init__(self, cli_sock, name):
		threading.Thread.__init__(self)
		self.cli_sock = cli_sock
		self.name = name
		self.alive = True

	def run(self):
		# Keep the receive streaming socket open
		while self.alive:
			# Check if there is something to read on the socket
			# or if the socket has thrown exceptions for 20s
			rlist, wlist, xlist = select.select(
				[self.cli_sock], [], [self.cli_sock], 20)
			if rlist and not xlist:
				# Receive data on the socket
				print self.cli_sock.recv(100)
		# Close this client socket
		self.cli_sock.close()

	def stop(self):
		self.alive = False
	
	def get_name(self):
		return self.name

net_srv = NetworkServer()
net_srv.receive()
