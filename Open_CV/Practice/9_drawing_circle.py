import numpy as np
import cv2
import matplotlib.pyplot as plt

img_path = r'my pic.jpg'
img = cv2.imread(img_path)
cv2.imshow('Orignal image',img)

#Draw a line on image
# cv2.line(image, start_point, end_point, color, thickness)
# image: It is the image on which line is to be drawn.
# start_point: It is the starting coordinates of line. The coordinates are represented as tuples of two values i.e. (X coordinate value, Y coordinate value).
# end_point: It is the ending coordinates of line. The coordinates are represented as tuples of two values i.e. (X coordinate value, Y coordinate value).
# color: It is the color of line to be drawn. For BGR, we pass a tuple. eg: (255, 0, 0) for blue color.
# thickness: It is the thickness of the line in px.

#Draw a circle on image

center_coordinates = (330,230)
radius = 110
color = (255,0,0)
thickness = 5

circle_image = cv2.circle(img, center_coordinates, radius, color, thickness)
cv2.imshow('Circle image',circle_image)

cv2.waitKey(0)
cv2.destroyAllWindows()