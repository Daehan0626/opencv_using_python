import argparse
import cv2


parser=argparse.ArgumentParser()
parser.add_argument('--path',default='./data/Lena.png',help='Image path.')
params = parser.parse_args()

img=cv2.imread('./data/Lena.png')
cv2.imwrite('./data/Lena_compressed.png',img,[cv2.IMWRITE_PNG_COMPRESSION,0])

# saved_img=cv2.imread(params.out_png)
# assert saved_img.all()==img.all()

cv2.imwrite('./data/Lena_compressed.jpg',img,[cv2.IMWRITE_JPEG_QUALITY,0])

