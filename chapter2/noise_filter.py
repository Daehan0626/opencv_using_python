import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('./data/lena.png').astype(np.float32)/255

noised =(image + 0.2 * np.random.rand(*image.shape).astype(np.float32))
noised = noised.clip(0,1)
plt.imshow(noised[:,:,[2,1,0]])
plt.show()

gauss_blur = cv2.GaussianBlur(noised,(7,7),0) 
#GaussianBlur(입력 이미지,(커널사이즈),시그마값) 
plt.imshow(gauss_blur[:,:,[2,1,0]])
plt.show()

bilat = cv2.bilateralFilter(noised,-1,0.3,10)
#bilateralFilter(입력이미지,커널크기,색공간 표준편차, 거리공간 표준편차 )
#커널 크기가 음수면 거리공간 시그마 갑슬 사용해 계산함
plt.imshow(bilat[:,:,[2,1,0]])
plt.show()

