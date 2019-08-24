import cv2
import numpy as np
import matplotlib.pyplot as plt

gray = cv2.imread('./data/lena.png',0)
cv2.imshow('original gray',gray)
cv2.waitKey()
cv2.destroyAllWindows()

hist, bines = np.histogram(gray,256,[0,255])

plt.fill(hist)
plt.xlabel('pixel value')
plt.show()