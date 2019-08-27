import  cv2
import numpy as np

img=cv2.imread('./data/bnw.png',cv2.IMREAD_GRAYSCALE)
connetivity = 8
num_labels, labelmap = cv2.connectedComponents(img, connetivity,cv2.CV_32S)

#요소 번호의 튜플, 요소의 레이블을 포함한 이미지
# labelmap 입력이미지와 동일한 크기, [0,요소개수]
img=np.hstack((img, labelmap.astype(np.float32)/(num_labels)))
cv2.imshow('Connrcted components',img)
cv2.waitKey()
cv2.destroyAllWindows()

img=cv2.imread('./data/lena.png',cv2.IMREAD_GRAYSCALE)
otsu_thr, otsu_mask=cv2.threshold(img,-1,1,cv2.THRESH_BINARY|cv2.THRESH_OTSU)

output =cv2.connectedComponentsWithStats(otsu_mask,connetivity,cv2.CV_32S)

num_labels, labelmap, stats, centers=output

# 요소 번호의 튜플, 요소의 레이블을 포함한 이미지 , 중심위치
# stats = (요소갯수, 5) 5=(x0,y0,width,height,area)
# centers = (요소갯수, 2) 2=(x,y)
colored = np.full((img.shape[0], img.shape[1],3),0,np.uint8)

for l in range(1, num_labels):
    if stats[l][4]>200:
        colored[labelmap==l]=(0,255*l/num_labels,255*num_labels)
        cv2.circle(colored,(int(centers[l][0]),int(centers[l][1])),5,(255,0,0),cv2.FILLED)
        img =cv2.cvtColor(otsu_mask*255, cv2.COLOR_GRAY2BGR)

cv2.imshow('Connected components',np.hstack((img,colored)))
cv2.waitKey()
cv2.destroyAllWindows()

    