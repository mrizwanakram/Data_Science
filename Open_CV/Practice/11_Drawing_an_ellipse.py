import numpy as np
import cv2
import matplotlib.pyplot as plt

img_path = r'my pic.jpg'
img = cv2.imread(img_path)
cv2.imshow('Orignal image',img)

#Draw an ellipse

color = (255,0,0)
thickness = 2
center_coordinates = (80,100)
axesLength = (100,50)
angle = 30
startAngle = 40
endAngle = 360
ellipse_image = cv2.ellipse(img, center_coordinates, axesLength, angle, startAngle, endAngle, color, thickness)

cv2.imshow('Ellipse image',ellipse_image)
cv2.waitKey(0)
cv2.destroyAllWindows()