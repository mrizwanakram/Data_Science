import cv2
import numpy as np
import matplotlib.pyplot as plt

img_path = r'my pic.jpg'
img = cv2.imread(img_path)
cv2.imshow('Orignal image',img)

#Resize_image

resize = cv2.resize(img, (300,300))
cv2.imshow('Resize image',resize)

cv2.waitKey(0)
cv2.destroyAllWindows()