import math
import numpy
import threading
from time import sleep
from database_handler import DatabaseHandler

class Trilateration(threading.Thread):
	"""A class computing a tags position based on reader measurements"""
	
	def __init__(self):
		threading.Thread.__init__(self)
		self.db_hdlr = DatabaseHandler('measurements.db')
		self.alive = True

	def run(self):
		while self.alive:
			rowcount = self.db_hdlr.get_rowcount()
			if rowcount < 3:
				continue
			positions = self.db_hdlr.get_positions()
			readings = self.db_hdlr.get_readings()
			self.trilateration(positions, readings)	
			sleep(3)
		self.db_hdlr.close_db()

	def stop(self):
		self.alive = False

	def rss_to_dist(self, readings):
		dists = []
		for node_name, rss in readings:
			dist = 1 / math.sqrt(rss)
			self.db_hdlr.update_dist(node_name, dist)
			dists.append(dist)
			print 'Node', node_name, 'with rss', rss, 'has dist', dist
		return dists

	def trilateration(self, positions, readings):
		maxzero = 0.0

		p1 = numpy.array(positions[0])
		p2 = numpy.array(positions[1])
		p3 = numpy.array(positions[2])
		
		r1, r2, r3 = self.rss_to_dist(readings)
		
		ex = p2 - p1
		# d = |p2 - p1|
		d = numpy.linalg.norm(ex)

		if d <= maxzero:
			# p1 and p2 are concentric
			print 'p1 and p2 are concentric'
			return
		
		# ex = (p2 - p1) / |p2 - p1|
		ex = ex / d
		
		# t1 = p3 - p1
		t1 = p3 - p1
		# i = ex . (p3 - p1)
		i = numpy.dot(ex, t1)
		# t2 = ex(ex . (p3 - p1))
		t2 = ex * i

		# ey = p3 - p1 - ex(ex . (p3 - p1))
		ey =  t1 - t2
		# t = |p3 - p1 - ex(ex . (p3 - p1))|
		t = numpy.linalg.norm(ey)
		
		if t > maxzero:
			# p1, p2, p3 are not collinear

			# ey = (t1 - t2) / |t1 - t2|
			ey = ey / t

			# j = ey . (p3 - p1)
			j = numpy.dot(ey, t1)
		else:
			j = 0.0
		
		if math.fabs(j) <= maxzero:
			# p1, p2, p3 are collinear
			
			# Is point p1 +/- (r1 along the axis) the intersection?
			ts = [p1 + ex*r1, p1 - ex*r1]
			for t in ts:
				if ((math.fabs(numpy.linalg.norm(p2 / t) - r2) <= maxzero) and
					(math.fabs(numpy.linalg.norm(p3 / t) - r3) <= maxzero)):
					p = t
					print 'p1, p2, p3 are collinear'
					print 'p1 +/- ex*r1 is the only intersection point'
					print 'p', p
					return
			print 'p1, p2, p3 are collinear but no solution exists'
			return
		
		# ez = ex x ey	
		ez = numpy.cross(ex, ey)

		print 'ex', ex
		print 'ey', ey
		print 'ez', ez
		print 'd', d
		print 'i', i
		print 'j', j
		
		# x = (r1^2 - r2^2) / 2d +  d / 2
		x = (math.pow(r1, 2) - math.pow(r2, 2)) / (2*d) + d / 2
		
		print 'x', x
		
		# y = (r1^2 - r3^2 + i^2) / (2*j) + j / 2 - x * i / j
		y = ((math.pow(r1, 2) - math.pow(r3, 2) + math.pow(i, 2)) / (2*j) 
			+ j / 2  - x * i / j)
		
		print 'y', y

		# z = r1^2 - x^2 - y^2
		z = math.pow(r1, 2) - math.pow(x, 2) - math.pow(y, 2)

		# Check the sign of the z dimension
		if z < -maxzero:
			print 'The solution is invalid'
			return
		elif z > maxzero:
			z = math.sqrt(z)
		else:
			z = 0

		print 'z', z
		
		t = p1 + x*ex + y*ey
		
		p = t + z*ez
		print 'p', p
		
		p = t - z*ez
		print 'p', p


