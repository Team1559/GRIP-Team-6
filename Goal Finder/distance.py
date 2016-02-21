
from __future__ import division
import numpy as np
from decimal import Decimal


distancelist = [77, 4, 134, 5, 182, 6, 219, 7, 258, 8, 286, 9, 319, 10, 338, 11, 352, 12, 372, 13, 387, 14, 395, 15, 406, 16, 420, 17, 433, 18]
global distance
distance = 0.0
index = 0


def findDistance(y):


	#go through scan line list
	for i in range(0, len(distancelist), 2):
		if(y > distancelist[i]):
			distance = distancelist[i+1]

		else:
			if i > len(distancelist):
				print "Error: no distance found"
				distance = 0
				return distance
			break


	#interpolate to find accurate-ish distant
	index = distancelist.index(distance)
	y1 = distancelist[index+1]
	y2 = distancelist[index-1]
	slope = 1/(y1-y2)

	if(slope < 0):
		slope * -1

	#plug in to linear formula
	yint = distance - (slope * y2)
	distance = (slope * y) + yint

	return distance






