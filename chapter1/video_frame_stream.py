import cv2

capture = cv2.VideoCapture('./data/drop.avi')

while True:
    has_frame, frame = capture.read()
    if not has_frame:
        print('Reached the end of the video')
        break
    cv2.imshow('frame',frame)
    key = cv2.waitKey(50)
    if key==27:
        print('Pressed Esc')
        break
cv2.destroyWindow()

