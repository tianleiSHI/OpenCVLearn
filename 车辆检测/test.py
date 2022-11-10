import cv2
import numpy as np
import os

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
'''TrackBar控件'''


def callback(value):
    print(value)


cv2.namedWindow('trackbar', cv2.WINDOW_NORMAL)

cv2.createTrackbar('R', 'trackbar', 0, 255, callback)
cv2.createTrackbar('G', 'trackbar', 0, 255, callback)
cv2.createTrackbar('B', 'trackbar', 0, 255, callback)

img = np.zeros((480, 640, 3), np.uint8)
while True:
    r = cv2.getTrackbarPos('R', 'trackbar')
    g = cv2.getTrackbarPos('G', 'trackbar')
    b = cv2.getTrackbarPos('B', 'trackbar')
    img[:] = [b, g, r]

    cv2.imshow('trackbar', img)
    key = cv2.waitKey(10000)
    print(key)
    if key & 0xff == ord('q'):
        break
cv2.destroyAllWindows()
cv2.waitKey(1)
print('程序结束')