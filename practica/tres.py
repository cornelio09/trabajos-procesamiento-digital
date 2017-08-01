import cv2
imagen = cv2.imread('grupo.jpg')
hsv_imagen=cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV image',hsv_imagen)
cv2.imshow('Hue channel',hsv_imagen[:,:,0])
cv2.imshow('Saturacion channel',hsv_imagen[:,:,1])
cv2.imshow('Value channel',hsv_imagen[:,:,2])
cv2.waitKey()
cv2.destroyAllWindows()
