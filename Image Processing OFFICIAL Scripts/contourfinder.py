import cv2
import numpy as np
import time
import logging
logging.basicConfig(level=logging.DEBUG)
import server

cx = 0
cy = 0

s = server.Server()

# create video capture
cap = cv2.VideoCapture(0)



while(1):
	



    # read the frames #
    _,frame = cap.read()

    # smooth it #
    frame = cv2.blur(frame,(3,3))
    #frame = cv2.resize(640, 480)

    # convert to hsv and find range of colors #
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    thresh = cv2.inRange(hsv,np.array((79,14,138)), np.array((180,255,238)))
    thresh2 = thresh.copy()

    # find contours in the threshold image #
    contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

    # finding contour with maximum area and store it as best_cnt #
    max_area = 0
    best_cnt = None
    
    for i, cnt in enumerate(contours):
        if i > 100:
            break
        area = cv2.contourArea(cnt)
        if area > max_area:
            max_area = area
            best_cnt = cnt
        
    if best_cnt == None:
         cx = cy = -1
         print "Nothing Found"
    else:
    	# finding centroids of best_cnt and draw a circle there #
    	M = cv2.moments(best_cnt)
    	hull_cnt = cv2.convexHull(best_cnt)
    	#print max_area/cv2.contourArea(hull_cnt)
    	cv2.drawContours(frame, hull_cnt, -1, (0,255,0), 3)
    	cx,cy = int(M['m10']/M['m00']), int(M['m01']/M['m00'])
    	cv2.circle(frame,(cx,cy),5,255,-1)



	#socket setup
    #data = s.receive()
    #if data:
    s.accept()
    s.send(cx, cy)
    s.close()
        

	#print for testing
    print cx
    print cy
    print 


# Clean up everything before leaving
server.close()
cv2.destroyAllWindows()
cap.release()
