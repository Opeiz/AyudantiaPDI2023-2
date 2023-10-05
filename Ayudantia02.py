import cv2
import numpy as np

# image = cv2.imread("C:/Ayudantia-PDI/AyudantiaPDI2022-2/Images/Image08.jpg")

# cols = image.shape[1]
# rows = image.shape[0]
# image = cv2.resize(image, (cols//4, rows//4))
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Gaussian = cv2.GaussianBlur(gray, (x, x), cv2.BORDER_DEFAULT)

# Median = cv2.medianBlur(gray, x)

# th1 = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY)[1]
# th2 = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY_INV)[1]

cap = cv2.VideoCapture(0)
# hsv = None
# frame = None
# hsv2 = None
# hsv3 = None

while True:
    ret, frame = cap.read()

    cv2.imshow("original frame", frame)

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsv = cv2.inRange(frame, (20, 0, 50), (40, 255, 255))
    hsv2 = cv2.erode(hsv, cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7)))
    hsv3 = cv2.dilate(hsv2, cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7)))

    cv2.imshow("Filter", hsv3)

    if cv2.waitKey(10) == 27:
        break

cv2.destroyAllWindows()