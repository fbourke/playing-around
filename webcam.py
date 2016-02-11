import cv2
import numpy as np
import random
import time
import sys

if len(sys.argv) > 1:
	cascPath = sys.argv[1]
else:
	cascPath = './haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)
start = time.time()
while True:
	# Capture frame-by-frame
	ret, frame = video_capture.read()

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	faces = faceCascade.detectMultiScale(
		gray,
		scaleFactor=1.1,
		minNeighbors=5,
		minSize=(30, 30),
		flags=cv2.cv.CV_HAAR_SCALE_IMAGE
	)
	random.seed()
	# Draw a rectangle around the faces
	for (x, y, w, h) in faces:
		cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
		color = cv2.cv.Scalar(random.randint(0,255), random.randint(0,255), random.randint(0,255));
		cv2.circle(frame, (x+w/2,y+h/2), w/2, color, 5)

	# Display the resulting frame
	looptime = 1/(time.time() - start)
	start = time.time()
	color = cv2.cv.Scalar(random.randint(0,255), random.randint(0,255), random.randint(0,255))
	cv2.putText(frame, 'Framerate: %.1f FPS' % looptime, (10,500), cv2.FONT_HERSHEY_DUPLEX, 1, color, 1)
	cv2.imshow('Video', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()