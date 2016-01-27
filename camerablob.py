import cv2
import numpy as np
#find shapes next time#

vc = cv2.VideoCapture(0)

#filter blobs
par = cv2.SimpleBlobDetector_Params()
par.filterByArea = True
par.minArea = 1000
par.filterByCircularity = True
par.minCircularity = .5
par.filterByConvexity = False
par.filterByInertia = False
detector = cv2.SimpleBlobDetector_create(par)

for x in range(0, 500): #500 frames of video

    #original image
    ret, img = vc.read()
    cv2.imshow("original image", img)

    #filter colors
    cimg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_color = np.array([79, 14, 138])
    upper_color = np.array([180, 255, 238])
    cimg = cv2.inRange(cimg, lower_color, upper_color)
    cv2.imshow("hsv", cimg)


    ###BROKEN###

    #filter lines
    #nimg = cv2.cvtColor(cimg, cv2.COLOR_HSV2BGR)
    #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #edges = cv2.Canny(gray, 50, 150)
    #lines = cv2.HoughLines(edges, 1, np.pi/180.0, 50, np.array([]), 0, 0)
    #a,b,c = lines.shape
    #for i in range(a):
        #rho = lines[i][0][0]
        #theta = lines[i][0][1]
        #a = np.cos(theta)
        #b = np.sin(theta)
        #x0, y0 = a*rho, b*rho
        #pt1 = ( int(x0+1000*(-b)), int(y0+1000*(a)) )
        #pt2 = ( int(x0-1000*(-b)), int(y0-1000*(a)) )
        #cv2.line(lines, pt1, pt2, (0, 0, 255), 3, cv2.LINE_AA)


    ###NOT USING###

    #filter blob image
    #keypoints = detector.detect(img)
    #kpi = cv2.drawKeypoints(img, keypoints, np.array([]), (0, 0, 225), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    #cv2.imshow("blobs", kpi)

    cv2.waitKey(1) & x #open frame for 1 ms
