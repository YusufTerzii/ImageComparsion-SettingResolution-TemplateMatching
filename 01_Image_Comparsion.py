import cv2
import numpy as np

img1 = cv2.imread("08_Alistirmalar2/images/aircraft.jpg")
img1 = cv2.resize(img1,(640,550))

img2 = cv2.imread("08_Alistirmalar2/images/aircraft (1).jpg")
img2 = cv2.resize(img2,(640,550))

img3= cv2.medianBlur(img1,7)

if img1.shape == img2.shape:
    print("Same size")
else:
    print("Not same Size")

diff = cv2.subtract(img1,img3)
b,g,r = cv2.split(diff)

if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:##It will count to  non zero numbers
    print("Completely Equal")

else:
    print("Not Completely Equal")

    ## Output is:
    ## Same size
    ## Not Completely Equal




cv2.imshow("img1",img1)
cv2.imshow("img2",img2)
cv2.imshow("diff",diff)

cv2.waitKey(0)
cv2.destroyAllWindows