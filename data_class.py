import time
import random
import numpy as np

class data:
	def __init__(self):
		self.timestamp = time.time()
		self.frameID = -1
		self.heigh = -1
		self.width = -1
		self.x = -1
		self.y = -1
		self.speed = -1
		self.direction = -1

	def set_data(self):
		self.timestamp = time.time()
		self.frameID = random.randint(0, 1024)
		self.heigh = random.randint(16, 2048)
		self.width = random.randint(16, 2048)
		self.x = random.randint(0, self.heigh)
		self.y = random.randint(0, self.width)
		self.speed = random.randint(0, np.max([self.heigh, self.width]))
		self.direction = random.randint(0, 359)
		

	def print(self):
		print('Timestamp:', self.timestamp)
		print('Frame ID:', self.frameID)
		print('Height:', self.heigh)
		print('Width:', self.width)
		print('X:', self.x)
		print('Y:', self.y)
		print('Speed:', self.speed)
		print('Direction:', self.direction)