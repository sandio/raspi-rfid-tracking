import select
import socket
import threading

class NetworkServer(threading.Thread):
	"""A class for receiving readings from the other Pis"""
	
	def __init__(self):
		threading.Thread.__init__(self)
		# Create an INET, STREAMing socket
		self.srv_sock = socket.socket(
			socket.AF_INET, socket.SOCK_STREAM)
		# Bind the socket to a public host and port
		self.srv_sock.bind(('0.0.0.0', 1234))
		# Become a server socket and queque max 5
		self.srv_sock.listen(5)
		self.alive = True
	
	def run(self):
		# A list of receive threads
		self.rcv_thrs = []
		fd = self.srv_sock.fileno()
		while self.alive:
			rlist, wlist, xlist = select.select(
				[fd], [], [fd], 5)
			if rlist and not xlist:
				# Accept connections from outside
				(cli_sock, addr) = self.srv_sock.accept()
				print 'Connection from', addr
				# Create a receive thread to handle this stream
				rcv_thr = RcvThread(cli_sock, addr)
				rcv_thr.start()
				# Append this thread to the other receive threads
				self.rcv_thrs.append(rcv_thr)
	
	def stop(self):
		self.alive = False
		# Go through the list of theads
		for rcv_thr in self.rcv_thrs:
			# Stop a thread by exiting its receiving loop
			rcv_thr.stop()
			print 'Stopping thread', rcv_thr.get_addr()
			# Wait for the thread to terminate for 30s
			rcv_thr.join(10)
			# Check if the thread has terminated
			if rcv_thr.isAlive():
				print 'Thread', rcv_thr.get_addr(), 'alive'
		# Close the server socket
		self.srv_sock.close()
		
class RcvThread(threading.Thread):
	"""A tread class that receives readings over the network"""

	def __init__(self, cli_sock, addr):
		threading.Thread.__init__(self)
		self.cli_sock = cli_sock
		self.addr = addr
		self.alive = True

	def run(self):
		# Keep the receive streaming socket open
		fd = self.cli_sock.fileno()
		while self.alive:
			# Check if there is something to read on the socket
			# or if the socket has thrown exceptions for 20s
			rlist, wlist, xlist = select.select(
				[fd], [], [fd], 20)
			if xlist:
				break
			if rlist:
				# Receive data on the socket
				data = self.cli_sock.recv(7)
				print data, len(data) 
		# Close this client socket
		self.cli_sock.close()

	def stop(self):
		self.alive = False
	
	def get_addr(self):
		return self.addr
