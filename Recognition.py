import cv2
import os
import numpy as np

face_cascade = cv2.CascadeClassifier(r"C:\Users\Yunus\Desktop\UDIS\HaarCascade\haarcascade_frontalface_alt2.xml")

cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

    for (x, y, w, h) in faces:
        print(x, y, w, h)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
        img_item = r"C:\Users\Yunus\Desktop\UDIS\recognition\TesstImages\ul.png"
        Caught_img = r"C:\Users\Yunus\Desktop\UDIS\recognition\TestImages\ul.png"
        cv2.imwrite(Caught_img, roi_gray)
        cv2.imwrite(img_item, roi_gray)
        color = (55, 250, 55)
        stroke = 2
        end_cord_x = x + w
        end_cord_y = y + h
        cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)

    # display the resulting frame
    cv2.imshow('Live Stream', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
# when everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
