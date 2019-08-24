import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2. imread('./data/lena.png',0).astype(np.float32)/255
#주파수 도메인으로 변환
fft = cv2.dft(image,flags=cv2.DFT_COMPLEX_OUTPUT)
#낮은 주파수가 배열의 중앙에 위치하도록 결과 이동
fft_shift = np.fft.fftshift(fft,axes=[0,1])
#고주파의 진폭을 0으로 설정
sz=25
mask = np.zeros(fft_shift.shape,np.uint8)
mask[mask.shape[0]//2-sz:mask.shape[0]//2+sz,mask.shape[1]//2-sz:mask.shape[1]//2+sz,:] = 1
fft_shift*=mask
#이산 푸리에 변환의 결과를 이동
fft =np.fft.ifftshift(fft_shift, axes=[0,1])
#역이산 푸리에 변환을 사용해 필터링된 이미지를 주파수 도메인에서 다시 공간 도메인으로 변환
filtered = cv2.idft(fft, flags=cv2.DFT_SCALE|cv2.DFT_REAL_OUTPUT)

plt.figure()
plt.subplot(121)
plt.axis('off')
plt.title('original')
plt.imshow(image,cmap='gray')
plt.subplot(122)
plt.axis('off')
plt.title('no high frequencies')
plt.imshow(filtered, cmap='gray')
plt.tight_layout()
plt.show()


