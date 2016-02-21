
from __future__ import division
import distance
import math


def getAngle(distance, error):

	#find pixels per feet at camera angle
	pixperft = 57/8

	#convert error into feet
	errorfeet = error * pixperft

	#find angle using triangle of camera and target
	var = errorfeet / distance
	radians = math.atan(var)
	angle = math.degrees(radians)

	return angle
