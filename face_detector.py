#pip install opencv-python
#haarcascade_frontalface_default.xml

import cv2

a = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

b = cv2.VideoCapture(0)

while True:
    c_rec, d_image = b.read()
    e = cv2.cvtColor(d_image,cv2.COLOR_BGR2GRAY)
    f = a.detectMultiScale(e, 1.3,6)

    for (X1,Y1,W1,h1) in f:
        cv2.rectangle(d_image,(X1,Y1), (X1+W1, Y1+h1), (0, 255,0), 10)

    cv2.imshow('img',d_image)
    h = cv2.waitKey(40) & 0xff
    if h == 40:
        break
b.release()
cv2.destroyAllWindows()