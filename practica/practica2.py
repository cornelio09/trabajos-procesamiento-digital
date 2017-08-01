import cv2
grayImage=cv2.imread('emoji.png', cv2.CV_LOAD_IMAGE_GRAYSCALE)
cv2.imwrite('myemogi.png', grayImage)

cv2.imshow('imagen',grayImage)

cv2.waitKey(0)
cv2.destroyAllWindows()
