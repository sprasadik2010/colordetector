# TechVidvan Object detection of similar color
import cv2
import numpy
import numpy as np
# Reading the image
img = cv2.imread('image.jpg',1)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
print(hsv)
cv2.imshow("Output", hsv)
cv2.waitKey(0)
