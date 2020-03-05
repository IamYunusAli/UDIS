import cv2
import os
import numpy as np
from tkinter import *
from tkinter import Label


from faceRecognition import facedetection, draw_rect, put_text, labels_for_training_data, train_classifier

test_img = cv2.imread('../TestImages/ul.png')
faces_detected,gray_img = facedetection(test_img)
#faces_detected, gray_img = facedetection(test_img)
print("The detected face:", faces_detected)

for (x, y, w, h) in faces_detected:
    cv2.rectangle(test_img, (x, y), (x + w, y + h), (255, 0, 0), thickness=1)

faces, faceID = labels_for_training_data('/home/darknet/PycharmProjects/Python/recognition/Trainingimages')
face_recognizer = train_classifier(faces, faceID)
name = {0: "Licensed", 1: "Unlicensed"}

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




##part of desktop appl ication
root = Tk()
root.geometry("1250x750+0+0")
root.title("Unlicensed Drivers Identification System")
root.configure(background='Cadet Blue')

Tops = Frame(root, bg='Cadet Blue', pady=2, width=1050, height=100, relief=RIDGE)
Tops.grid(row=0, column=0)

lblTitle: Label = Label(Tops, font=('Arial', 30, 'bold'), text="***Unlicensed Drivers Identification System***", bd=21,
                        bg='Cadet Blue', fg='Cornsilk', justify=CENTER)
lblTitle.grid(row=0, column=0)

MainFrame = Frame(root, bg='Powder Blue', bd=10, width=1300, height=550, relief=RIDGE)
MainFrame.grid(row=1, column=0)

LeftFrame = Frame(MainFrame, bd=10, width=800, height=510, pady=2, padx=10, bg="Cadet Blue", relief=RIDGE)
LeftFrame.pack(side=LEFT)

#pic = PhotoImage(file="ASTU.jpeg")
#lbl = Label(LeftFrame, image=pic)
#lbl.pack()

RightFrame = Frame(MainFrame, bd=10, width=300, height=480, padx=10, pady=2, bg="Cadet Blue", relief=RIDGE)
RightFrame.pack(side=RIGHT)

RightFrame1 = Frame(RightFrame, bd=10, width=200, height=200, padx=10, pady=2, bg="Cadet Blue", relief=RIDGE)
RightFrame1.grid(row=0, column=0)

RightFrame2 = Frame(RightFrame, bd=10, width=200, height=200, padx=10, pady=2, bg="Cadet Blue", relief=RIDGE)
RightFrame2.grid(row=1, column=0)

platenumber = IntVar()
plateDigit = StringVar()
platenumber.set(111011111)
plateDigit.set("A.D")

Platenum: Label = Label(RightFrame1, font=('Arial', 20, 'bold'), text="Vehicle-plate-number:", padx=2,
                        pady=2, bg='Cadet Blue')
Platenum.grid(row=0, column=0, sticky=W)
txt = Entry(RightFrame1, font=('arial', 16, 'bold'), bd=2, fg="black", textvariable=platenumber, width=8, justify=LEFT).grid(row=0, column=1)


DriverId: Label = Label(RightFrame1, font=('Arial', 20, 'bold'), text="Driver-Id-number:", padx=2,
                        pady=2, bg='Cadet Blue')
DriverId.grid(row=1, column=0, sticky=W)

txt2 = Entry(RightFrame1, font=('arial', 16, 'bold'), bd=2, fg="black", textvariable=platenumber, width=8, justify=LEFT).grid(row=1, column=1)



#RightFrame = Frame(MainFrame, bd=10, width =350, height=480, padx=10, pady=2, bg="Cadet Blue", relief=RIDGE)
#RightFrame.pack(side=RIGHT)


#RightFrame = Frame(MainFrame, bd=10, width =350, height=480, padx=10, pady=2, bg="Cadet Blue", relief=RIDGE)
#RightFrame.pack(side=RIGHT)

root.mainloop()
