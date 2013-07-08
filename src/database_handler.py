import sqlite3

class DatabaseHandler:
	"""A class for handling database queries"""

	def __init__(self, db):
		self.conn = sqlite3.connect(
			db, isolation_level=None, check_same_thread=False)
		self.cur = self.conn.cursor()
	
	def create_tbl(self):
		self.cur.execute('DROP TABLE IF EXISTS rfid')
		self.cur.execute('CREATE TABLE rfid(num INTEGER PRIMARY KEY, ' \
			'node_name INTEGER, tag_id TEXT, rss INTEGER)')
	
	def ins_into_tbl(self, node_name, tag_id, rss):
		self.cur.execute('INSERT INTO rfid(node_name, tag_id, rss) ' \
			'VALUES(?, ?, ?)', (node_name, tag_id, rss))

	def get_rowcount(self):
		c = self.cur.execute('SELECT * from rfid GROUP BY node_name')
		return len(c.fetchall())
	
	def get_readings(self):
		self.cur.execute('SELECT node_name, rss FROM rfid ' \
			'GROUP BY node_name')
		return self.cur.fetchall()

	def get_positions(self):
		self.cur.execute('SELECT x, y, z FROM positions ' \
			'GROUP BY node_name')
		return self.cur.fetchall()

	def update_dist(self, node_name, dist):
		self.cur.execute('UPDATE positions SET r = ? ' \
			'WHERE node_name = ?', (dist, node_name))

	def close_db(self):
		self.conn.close()
