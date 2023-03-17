import cv2
import numpy as np
import matplotlib.pyplot as plt

img_path = r'my pic.jpg'
img = cv2.imread(img_path)

cv2.imshow('Orignal image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()