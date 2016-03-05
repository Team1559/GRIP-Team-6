#!/usr/bin/python

###COMMAND LINE APPLICATION FOR TESTING WITH OPENCV HSV FILTERS###
###AUTHOR WILL MERGES###


import cv2
import sys
import Tkinter

#get supplied values for filter
hlow = sys.argv[1]
hhigh = sys.argv[2]
slow = sys.argv[3]
shigh = sys.argv[4]
vlow = sys.argv[5]
vhigh = sys.argv[6]

#set the image path to save calibration image
imgpath = "C:\Users\Will\Documents\Code\Python Code\Image Processing\Goal Finder\CalibrationPhotos"

#create the webcam
cam = cv2.VideoCapture(0)
cam.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 480)


while (1):

    #open the camera stream
    _,frame = cam.read()

    #convert to hsv with supplied values
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    hsv = cv2.inRange(hsv, np.array((hlow, slow, vlow)), np.array((hhigh, shigh, vhigh)))

    #save the image
    cv2.imwrite(imgpath)

    #view the image
    cv2.imshow("hsv", hsv)
    cv2.waitKey(1)
