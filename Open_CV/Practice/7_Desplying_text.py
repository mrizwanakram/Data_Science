import cv2
import numpy as np
import matplotlib.pyplot as plt

img_path = r'my pic.jpg'
img = cv2.imread(img_path)
print(img.shape)
# cv2.imshow('Orignal image',img)



# textimage = cv2.putText(img, 'M.Rizwan', (100, 630),cv2.FONT_HERSHEY_SIMPLEX, 3, (55, 55, 234), 10, cv2.LINE_AA)
text = 'M.Rizwan'
cord = (100, 630)
font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 3
color = (55, 55, 234)
thickness = 10
lineType = cv2.LINE_AA

textimage = cv2.putText(img, text, cord, font, fontScale, color, thickness, lineType)

cv2.imshow('Text image',textimage)

cv2.waitKey(0)
cv2.destroyAllWindows()