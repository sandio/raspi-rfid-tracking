import sqlite3

class DatabaseHandler:
	"""A class for handling database queries"""

	def __init__(self, db):
		self.conn = sqlite3.connect(
			db, isolation_level=None, check_same_thread=False)
		self.cur = self.conn.cursor()
	
	def flush_rss_readings(self):
		self.cur.execute('DROP TABLE IF EXISTS rfid')
		self.cur.execute('CREATE TABLE rfid(num INTEGER PRIMARY KEY, ' \
			'node_name INTEGER, tag_id TEXT, rss INTEGER)')

	def check_pos_tbl(self):
		self.cur.execute('SELECT name FROM sqlite_master ' \
			'WHERE type="table" AND name="positions"')
		if not self.cur.fetchone():
			self.cur.execute('CREATE TABLE positions(node_name INTEGER, ' \
				'x REAL, y REAL, z REAL, r REAL)')
			positions = [(0,0,0,0,1), (1,1,0,0,1), (2,1,1,0,1), (3,0,0,0,0)]
			for pos in positions:
				self.cur.execute('INSERT INTO positions ' \
					'VALUES(?,?,?,?,?)', pos)

	def check_rsl_tbl(self):
		self.cur.execute('SELECT name FROM sqlite_master ' \
			'WHERE type="table" AND name="results"')
		if not self.cur.fetchone():
			self.cur.execute('CREATE TABLE results(name TEXT, ' \
				'x REAL, y REAL, z REAL)')
			names = ['ex', 'ey', 'ez', 'd', 'i', 'j', 'x', 'y', 'z', 'p']
			for name in names:
				self.cur.execute('INSERT INTO results ' \
					'VALUES(?, 0, 0, 0)', [name])

	def ins_reading(self, node_name, tag_id, rss):
		self.cur.execute('INSERT INTO rfid(node_name, tag_id, rss) ' \
			'VALUES(?, ?, ?)', (node_name, tag_id, rss))

	def update_dist(self, node_name, dist):
		self.cur.execute('UPDATE positions SET r = ? ' \
			'WHERE node_name = ?', (dist, node_name))

	def update_pnt(self, pnt):
		self.cur.execute('UPDATE positions SET x = ?, ' \
			'y = ?, z = ? WHERE node_name = 3', pnt)

	def update_rsl(self, name, values):
		self.cur.execute('UPDATE results SET x = ? ' \
			'WHERE name = ?', (values, name))

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

	def close_db(self):
		self.conn.close()
