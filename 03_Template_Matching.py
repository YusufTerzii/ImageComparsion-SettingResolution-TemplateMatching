import cv2
import numpy as np

img = cv2.imread("08_Alistirmalar2/images/starwars.jpg")
template = cv2.imread("08_Alistirmalar2/images/starwars2.jpg",0)

w,h = template.shape[::-1]

gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

result = cv2.matchTemplate(gray_img,template,cv2.TM_CCOEFF_NORMED)
location = np.where(result>=0.99)

for points in zip(*location[::-1]):
    cv2.rectangle(img,points,(points[0]+w,points[1]+h),(0,255,0),3)





cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows
