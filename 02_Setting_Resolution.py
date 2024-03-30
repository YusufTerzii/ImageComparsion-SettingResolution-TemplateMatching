import cv2
import numpy as np

windowName = "Live Video"
cv2.namedWindow(windowName)

cam = cv2.VideoCapture(0)

print("Width : "+str(cam.get(3)))
print("Height : "+str(cam.get(2)))

cam.set(3,1280)
cam.set(4,720)

print("Width** : "+str(cam.get(3)))
print("Height** : "+str(cam.get(2)))

while True:
    ret, frame = cam.read()
    frame = cv2.flip(frame,1)

    cv2.imshow(windowName, frame)

    if cv2.waitKey(27) & 0xFF==ord("q"):
        break

cam.release()
cv2.destroyAllWindows()
