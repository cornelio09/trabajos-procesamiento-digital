import numpy as np
import cv2

img = cv2.imread('emoji.png')
cv2.imshow('emoji',img)

cv2.waitKey(0)
cv2.destroyWindows()
