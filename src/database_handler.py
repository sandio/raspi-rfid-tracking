import sqlite3

class DatabaseHandler:
	"""A class for handling database queries"""

	def __init__(self, db):
		self.conn = sqlite3.connect(db, isolation_level=None)
		self.cur = self.conn.cursor()
	
	def create_tbl(self):
		self.cur.execute('DROP TABLE IF EXISTS rfid')
		self.cur.execute('CREATE TABLE rfid(num INTEGER PRIMARY KEY, ' \
			'tag_id TEXT, rss INTEGER)')
	
	def ins_into_tbl(self, tag_id, rss):
		self.cur.execute('INSERT INTO rfid(tag_id, rss) ' \
			'VALUES(?, ?)', (tag_id, rss))

	def close_db(self):
		self.conn.close()
