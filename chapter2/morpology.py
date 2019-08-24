import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('./data/lena.png',0)
_,binary=cv2.threshold(image,-1,1,cv2.THRESH_BINARY|cv2.THRESH_OTSU)
#침식 팽창
eroded = cv2.morphologyEx(binary,cv2.MORPH_ERODE,(3,3),iterations=10)
dilated = cv2.morphologyEx(binary,cv2.MORPH_DILATE,(3,3),iterations=10)

#열림, 닫힘변환
opened = cv2.morphologyEx(binary,cv2.MORPH_OPEN,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5)),iterations=5)
closed = cv2.morphologyEx(binary,cv2.MORPH_CLOSE,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5)),iterations=5)

#형태학적 경사도 계산
grad=cv2.morphologyEx(binary,cv2.MORPH_GRADIENT,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5)))

plt.figure(figsize=(10,10))
plt.subplot(231)
plt.axis('off')
plt.title('bibary')
plt.imshow(binary,cmap='gray')

plt.subplot(232)
plt.axis('off')
plt.title('erode 10 times')
plt.imshow(eroded,cmap='gray')

plt.subplot(233)
plt.axis('off')
plt.title('dilate 10 times')
plt.imshow(dilated,cmap='gray')

plt.subplot(234)
plt.axis('off')
plt.title('open 5 times')
plt.imshow(opened,cmap='gray')

plt.subplot(235)
plt.axis('off')
plt.title('close 5 times')
plt.imshow(closed,cmap='gray')

plt.subplot(236)
plt.axis('off')
plt.title('gradient')
plt.imshow(grad,cmap='gray')

plt.tight_layout()
plt.show()