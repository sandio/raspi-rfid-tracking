from serial_connection import SerialConnection

class Main:
	"""A class for establishing connections"""
	
	def start_serial_con(self, port): 
		serial_con = SerialConnection(port)
		serial_con.open_port()
		serial_con.flush_input()
		serial_con.read_data()

	def stop_serial_con(self):
		serial_con.flush_input()
		serial_con.close_port()

main = Main()
main.start_serial_con('/dev/ttyUSB0')
