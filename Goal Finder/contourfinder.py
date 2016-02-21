#!/usr/bin/python

import cv2
import numpy as np
import time
import logging
logging.basicConfig(level=logging.DEBUG)
import serialserver
import sys
import math
import time
import angle
import distance


#log errors
sys.stderr.write("Image Processing Working\n")


#create video capture
cap = cv2.VideoCapture(0)
cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 480)
#cap.set(cv2.cv.CV_CAP_PROP_BRIGHTNESS, 0.0)


#create data to be sent
cx = 0
cy = 0
global error
global distance
global angle
error = 0
dist = 0.0
ang = 0.0

#open the server
serialserver.startServer()


while(1):

    #read the frames
    _,frame = cap.read()
    #cv2.imshow("cam", frame)
    #cv2.waitKey(5)

    #for calibration
    #cv2.imwrite("calibrate.png", frame)

    #convert to hsv and find range of colors
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    thresh = cv2.inRange(hsv,np.array((36,0,209)), np.array((69,9,255)))
    thresh2 = thresh.copy()

    #blur it
    thresh = cv2.blur(thresh, (7,7))

    #erode and dilate
    thresh = cv2.erode(thresh, (3,3))
    thresh = cv2.dilate(thresh, (3,3))

    #find contours in the threshold image
    contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

    # finding contour with maximum area and store it as best_cnt
    min_area = 1000
    best_cnt = None
    #max_area = 6000

    #sort by greatest areas
    contours = sorted(contours, key = cv2.contourArea, reverse = True)[:10]

    for i, cnt in enumerate(contours):
        if i > 100:
            break
        area = cv2.contourArea(cnt)
        if area == 0:
             continue

	#filter by ratio
        rx,ry,rw,rh = cv2.boundingRect(cnt)

        ratio = rw * rh / area
        if 2 < ratio < 4.2 and area > min_area:
            best_cnt = cnt
            print rw*rh / area

    #check if any shape was found
    if best_cnt == None:
         cx = cy = -1
         #print "Nothing Found"
    else:
    	#finding centroids of best_cnt and draw a circle there
    	M = cv2.moments(best_cnt)
    	hull_cnt = cv2.convexHull(best_cnt)
    	#print min_area/cv2.contourArea(hull_cnt)
    	cv2.drawContours(frame, hull_cnt, -1, (0,255,0), 3)
    	cx,cy = int(M['m10']/M['m00']), int(M['m01']/M['m00'])
    	cv2.circle(frame,(cx,cy),5,255,-1)


        #show the image
        #cv2.imshow("image", frame)
        #cv2.imshow("thresh", thresh2)
        #cv2.waitKey(5)


    #find the error, distance, and angle
    error = cx-320
	#make sure there is an object before finding distance and angle
    #if (cy > -1 and cx > -1):
		#dist = distance.findDistance(cy)
		#ang = angle.getAngle(dist, error)
    #else:
		#return -1 if no object is found
		#ang = dist = -1

    dist = 1
    ang = 1 #the last airbender
    #give values to server
    serialserver.putData(error)

    #show the image
    cv2.imshow("thresh", thresh2)
    cv2.imshow("frame", frame)
    cv2.waitKey(5)

    #print for testing
    print error
    #print cx
    #print cy
    #print distance
    #print angle

    #if cy != -1:
        #print cy

