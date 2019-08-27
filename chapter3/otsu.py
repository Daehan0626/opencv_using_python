import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('./data/lena.png',0)

otsu_thr,otsu_mask = cv2.threshold(image,-1,1,cv2.THRESH_BINARY|cv2.THRESH_OTSU)
print('Estimated theshold(Otsu):',otsu_thr)

plt.figure()
plt.subplot(121)
plt.axis('off')
plt.title('original')
plt.imshow(image,cmap='gray')
plt.subplot(122)
plt.axis('off')
plt.title('Otsu theshold')
plt.imshow(otsu_mask,cmap='gray')
plt.tight_layout()
plt.show()
