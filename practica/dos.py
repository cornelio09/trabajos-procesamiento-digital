import cv2
imagen=cv2.imread('grupo.jpg')
cv2.imshow('original', imagen)
cv2.waitKey()
gray_color=cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
cv2.imshow('GrayScale',gray_color)
cv2.waitKey()
cv2.destroyAllWindows()
