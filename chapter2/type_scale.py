import cv2, numpy as np

image = cv2.imread('./data/lena.png')
print('Shape:',image.shape)
print('Data type',image.dtype)

cv2.imshow('image', image)
cv2.waitKey()
cv2.destroyAllWindows()

image=image.astype(np.float32)/255
print('Shape:',image.shape)
print('Data type:', image.dtype)
cv2.imshow('imshow', np.clip(image*2,0,1))
cv2.waitKey()
cv2.destroyWindow()

image=(image*255).astype(np.uint8)
print('Shape:',image.shape)
print('Data type:', image.dtype)
cv2.imshow('image', image)
cv2.waitKey()
cv2.destroyWindow()


