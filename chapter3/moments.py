import cv2
import numpy as np
import matplotlib.pyplot as plt

image =np.zeros((480,640),np.uint8)
cv2.ellipse(image,(320,240),(200,100),0,0,360,255,-1)

m = cv2.moments(image)

for name, val in m.items():
    print(name,'\t',val)

print('Center X estimated :',m['m10']/m['m00'])
print('Center y estimated :',m['m01']/m['m00'])

# 이미지 모멘트는 컨투어에 관한 특징값을 뜻한다. OpenCV에서는 moments 함수로 이미지 모멘트를 구한다. 
# 컨투어 포인트 배열을 입력하면 해당 컨투어의 모멘트를 딕셔너리 타입으로 반환한다. 
# 반환하는 모멘트는 총 24개로 10개의 위치 모멘트, 7개의 중심 모멘트, 7개의 정규화된 중심 모멘트로 이루어져 있다.

# Spatial Moments : M00, M01, M02, M03, M10, M11, M12, M20, M21, M30
# Central Moments : Mu02, Mu03, Mu11, Mu12, Mu20, Mu21, Mu30
# Central Normalized Moments : Nu02, Nu03, Nu11, Nu12, Nu20, Nu21, Nu30