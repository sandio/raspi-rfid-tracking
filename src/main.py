import threading
from database_handler import DatabaseHandler
from network_server import NetworkServer
from serial_connection import SerialConnection

class Main:
	"""A class for establishing connections"""

	def start_db_hdlr(self, db):
		self.db_hdlr = DatabaseHandler(db)
		self.db_hdlr.create_tbl()

	def start_net_srv(self):
		self.net_srv = NetworkServer()
		self.net_srv.start()

	def start_serial_conn(self, port, timeout): 
		self.serial_conn = SerialConnection(port, timeout)
		self.serial_conn.open()
		self.serial_conn.flush_input()
	
	def run(self):
		try:
			while True:
				data = self.serial_conn.read().strip()
				tag_id = data[:4]
				rss = data[4:]
				self.db_hdlr.ins_into_tbl(tag_id, rss)
		except KeyboardInterrupt:
			self.db_hdlr.close_db()
			self.net_srv.stop()
			self.net_srv.join(30)
			self.serial_conn.close()

main = Main()
main.start_db_hdlr('measurements.db')
main.start_net_srv()
main.start_serial_conn('/dev/ttyUSB0', 30)
main.run()
