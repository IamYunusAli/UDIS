import cv2
import os
import numpy as np
from tkinter import *
from tkinter import Label


from faceRecognition import faceDetection, draw_rect, put_text, labels_for_training_data, train_classifier

test_img = cv2.imread("TestImages/ul.png")
faces_detected, gray_img = faceDetection(test_img)
print("The detected face:", faces_detected)

for (x, y, w, h) in faces_detected:
    cv2.rectangle(test_img, (x, y), (x + w, y + h), (255, 0, 0), thickness=1)

faces, faceID = labels_for_training_data("Trainingimages")
face_recognizer = train_classifier(faces, faceID)
name = {0: "Status:Licensed"
           "Country:Ethipian", 1: "Status:Unlicensed"
                                  "Country:Ethiopian"}

for face in faces_detected:
    (x, y, w, h) = face
    roi_gray = gray_img[y:y + h, x:x + h]
    lable, confidence = face_recognizer.predict(roi_gray)
    print("confidence:", confidence)
    print("lable:", lable)
    draw_rect(test_img, face)
    predicted_name = name[lable]
    put_text(test_img, predicted_name, x, y)

resized_img = cv2.resize(test_img, (600, 400))
cv2.imshow("UDIS", resized_img)
#cv2.imshow("UDIS", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows


#RightFrame = Frame(MainFrame, bd=10, width =350, height=480, padx=10, pady=2, bg="Cadet Blue", relief=RIDGE)
#RightFrame.pack(side=RIGHT)


#RightFrame = Frame(MainFrame, bd=10, width =350, height=480, padx=10, pady=2, bg="Cadet Blue", relief=RIDGE)
#RightFrame.pack(side=RIGHT)

