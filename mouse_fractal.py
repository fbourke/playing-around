import cv2
import numpy as np
import random
import time
import sys
import math


#===================== Function Defs ================================================

# GLOBALS
finish = False
color_count = 0
length = 10

def drawSnowflake(x,y):
	theta = random.randint(1,100)/100.0
	start = time.time()
	for i in range(0,6):
		theta += np.pi/3
		recursiveTree(x,y,theta,1)
	print 'Snowflake generation in {:.3f} seconds'.format(time.time()-start)

def recursiveTree(start_x,start_y,theta,depth): 
	max_depth = 4
	if depth > max_depth:
		return
	x = start_x
	y = start_y
	d = depth
	global finish
	finish = True
	(new_x, new_y) = drawPolarLine((x,y), length/d, theta)
	cv2.imshow('image', image)
	if not finish:
		key = cv2.waitKey(0)
	else:
		key = 0
	offset = 0
	threshold = 0
	branches = 1
	total_angle = np.pi/3
	for i in range(1,branches+2):
		if random.randint(0,255) > threshold:
			recursiveTree(new_x, new_y, theta + (i-1)*total_angle/branches - total_angle/2 + offset, d+1)	

def drawPolarLine((start_x,start_y), r, theta):
	x_len = r*np.cos(theta)
	y_len = r*np.sin(theta)
	color = getColor()
	cv2.line(image, (start_x,start_y), (int(start_x+x_len), int(start_y+y_len)), color, thickness=2)
	return (int(start_x+x_len), int(start_y+y_len))

def getColor():
	# uncomment for random color
	# return cv2.cv.Scalar(random.randint(0,255), random.randint(0,255), random.randint(0,255))
	# uncomment for red-ish color (autumn theme)
	# return cv2.cv.Scalar(random.randint(0,75), random.randint(20,200), random.randint(170,255))
	# uncomment for blue-ish
	# return cv2.cv.Scalar(random.randint(170,255), random.randint(20,200), random.randint(0,75))
	global color_count
	color_count += 1
	if color_count > 85*5:
		color_count = 0
	blue = color_count/5+170
	green = blue/2 + random.randint(0,125)
	red = random.randint(0,75)
	return cv2.cv.Scalar(blue, green, red)

# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode,length

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
        length = random.randint(5,60)
        drawSnowflake(ix,iy)
        print "Caught MouseDown"

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        # length = math.hypot(x-ix, y-iy)
        # angle = np.arctan2(y-iy, x-ix)
        # recursiveTree(ix, iy, angle, 1)
        # length = 50
        # drawSnowflake(ix,iy)
        print "Caught MouseUp"

def helpFunction():
	global image
	saved = image
	hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) #convert it to hsv
	h, s, v = cv2.split(hsv)
	v -= 100
	h -= 100
	final_hsv = cv2.merge((h, s, v))
	image = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
	cv2.putText(image, 'Window should be dim', (10,500), cv2.FONT_HERSHEY_DUPLEX, 1, getColor(), 1)
	cv2.line(image, (10,10), (100, 100), getColor(), thickness=2)
	cv2.line(image, (15,15), (150, 150), getColor(), thickness=2)
	drawPolarLine((100,123), 100, 0.5)
	# cv2.imshow('image',saved)
	print "should be dim now"
	k = 0
	while k != ord('x'):
		k = cv2.waitKey(1) & 0xFF
	    # if k == ord('x'):
	    	# return
		cv2.imshow('image', image)
	image = saved
	cv2.imshow('image', image)
	print "leaving help_function"
	# time.sleep(1)
	# print "slept 1"
	# # cv2.imshow('image',saved)
	# time.sleep(1)
	# print "slept 2"


#===================== Main Program ===============================================================

drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1
height,width = 600,800

image = blank_image = np.zeros((height,width,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',image)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == ord('c'):
    	image = np.zeros((height,width,3), np.uint8)
    	cv2.imshow('image',image)
    elif k == ord('r'):
    	length = random.randint(5,60)
    	drawSnowflake(random.randint(0,width),random.randint(0,height))
    elif k == ord('d'):
    	saved = image
    	helpFunction()
    	# time.sleep(1)
    	# image = saved
    	# cv2.imshow('image',image)
    elif k == 27 or k == ord('q'):
        break

cv2.destroyAllWindows()


# generate blank image
# width = 800
# height = 600
# image = blank_image = np.zeros((height,width,3), np.uint8)
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # make a starting dot
# x = width/2
# y = height-10
# cv2.circle(image, (x,y), 2, (0,255,0))

# # make some lines
# # depth = 1

# length = 200
# start_theta = 3*np.pi/2

# cv2.imshow('video', image)

# recursiveTree(x, y, start_theta, 1)
# time.sleep(1)

# cv2.imshow('video', image)
# cv2.waitKey(0)
