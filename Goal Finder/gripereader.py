
import sys
import numpy as np


class Reader(object):

	path = "/media/pi/WILL/config.gripe"


	def __init__(self):
		
		with open(self.path, "r") as self.target:
			self.read()
		
	
	def read(self):
		
		self.target.seek(0)
		stringlist = self.target.readlines()

		hlow = int(stringlist[0])
		slow = int(stringlist[1])
		vlow = int(stringlist[2])
		hhigh = int(stringlist[3])
		shigh = int(stringlist[4])
		vhigh = int(stringlist[5])

		self.brightness = float(stringlist[6])
		self.lowValue = np.array((hlow,slow,vlow))
		self.highValue = np.array((hhigh,shigh,vhigh))


	def getLowValue(self):
		return self.lowValue

	def getHighValue(self):
		return self.highValue

	def getBrightness(self):
		return self.brightness








	
