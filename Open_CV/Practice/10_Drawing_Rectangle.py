import numpy as np
import cv2
import matplotlib.pyplot as plt

img_path = r'my pic.jpg'
img = cv2.imread(img_path)
cv2.imshow('Orignal image',img)

#Draw a Rectangle on image
#cv2.rectangle(image, start_point, end_point, color, thickness)
#start_point: It is the starting coordinates of rectangle. The coordinates are represented as tuples of two values i.e. (X coordinate value, Y coordinate value).
#end_point: It is the ending coordinates of rectangle. The coordinates are represented as tuples of two values i.e. (X coordinate value, Y coordinate value).
#color: It is the color of rectangle to be drawn. For BGR, we pass a tuple. eg: (255, 0, 0) for blue color.
#thickness: It is the thickness of the rectangle line in px. If -1 is passed for closed rectangle, it will fill the rectangle shape. default thickness = 1

#Draw a Rectangle on image
start_point = (200,100)
end_point = (450,350)
color = (255,0,0)
thickness = 5
rectangle_image = cv2.rectangle(img, start_point, end_point, color, thickness)

cv2.imshow('Rectangle image',rectangle_image)
cv2.waitKey(0)
cv2.destroyAllWindows()