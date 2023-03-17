import cv2
import numpy as np
import matplotlib.pyplot as plt

img_path = r'my pic.jpg'
img = cv2.imread(img_path)

cv2.imshow('Orignal image',img)
#save image

# directory = r'C:\Users\user\Desktop\Python\OpenCV'
filename = 'Saving_my pic2.jpg'
cv2.imwrite(filename, img)
print('Saved')

cv2.waitKey(0)
cv2.destroyAllWindows()