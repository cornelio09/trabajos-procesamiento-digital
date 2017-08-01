import cv2
import numpy as np
from matplotlib import pyplot as plt

imagen = cv2.imread('grupo.jpg')
histogram = cv2.calcHist([imagen],[0],None,[256],[0,256])

plt.hist(imagen.ravel(),256,[0,256]); plt.show()

color = ('b','g','r')

for i, col in enumerate(color):
    histogram2 = cv2.calcHist([imagen],[0], None,[256],[0,256])

    plt.plot(histogram2,color=col)
    plt.xlim([0,256])

plt.show()
