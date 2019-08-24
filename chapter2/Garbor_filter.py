import math
import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('./data/lena.png',0).astype(np.float32)/255

kernel =cv2.getGaborKernel((21,21),5,1,10,1,0,cv2.CV_32F)
#커널 크기, 가우시안 표준편차, 파형방형, 파형길이, 공간비율, 위상
#가버 필터는 엣지검출
kernel/= math.sqrt((kernel * kernel).sum())

filterd = cv2.filter2D(image,-1,kernel)

plt.figure(figsize=(8,3))
plt.subplot(131)
plt.axis('off')
plt.title('image')
plt.imshow(image,cmap='gray')
plt.subplot(132)
plt.axis('off')
plt.title('kernel')
plt.imshow(kernel,cmap='gray')
plt.subplot(133)
plt.axis('off')
plt.title('filterd')
plt.imshow(filterd,cmap='gray')

plt.tight_layout()
plt.show()
