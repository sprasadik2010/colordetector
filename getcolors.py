
import cv2
import numpy
import numpy as np
# Reading the image
img = cv2.imread('image.jpg',1)
hsvs = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hsvarray = []
for hsv in hsvs:
    for item in hsv:
        hsvarray.append(item[2])

uniquehsaarray = [*set(hsvarray)]
print(uniquehsaarray)