import cv2
import numpy as np

capture_img = cv2.VideoCapture(0)
capture_img.set(10, 500)

def empty(a):
    pass
# Trackbar creating for maintaining the color shades of the images
path = 'images/car.jpg'
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 240)
cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 26, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBars", 21, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)
cv2.createTrackbar("Val Min", "TrackBars", 58, 255, empty)
cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)

#blue pen color---- 84, 149, 65, 255, 118, 255
#black pen---- 0, 179, 0, 255, 0, 95

while True:
    ret, img = capture_img.read()
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    sat_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    sat_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    val_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    val_max = cv2.getTrackbarPos("Val Max", "TrackBars")
    print(h_min, h_max, sat_min, sat_max, val_min, val_max)
    lower = np.array([h_min, sat_min, val_min])
    upper = np.array([h_max, sat_max, val_max])
    mask = cv2.inRange(imgHSV, lower, upper)

    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    stacked_img = np.hstack([img, mask])
    cv2.imshow("LIVE", stacked_img)
    if cv2.waitKey(1) == ord("t"):
        break

capture_img.release()
cv2.destroyAllWindows()

