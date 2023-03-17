import cv2
import numpy as np
import matplotlib.pyplot as plt

img_path = r'my pic.jpg'
img = cv2.imread(img_path)
cv2.imshow('Orignal image',img)

#gray_image

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray image',gray)

cv2.waitKey(0)
cv2.destroyAllWindows()