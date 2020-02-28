import cv2
import os
import numpy as np
from tkinter import *
from tkinter import Label

root = Tk()

root.geometry("1250x750+0+0")
root.title("Unlicensed Drivers Identification System")
root.configure(background='Cadet Blue')

def stream():
    face_cascade = cv2.CascadeClassifier('/home/darknet/Desktop/UDIS/HaarCascade/haarcascade_frontalface_alt2.xml')

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

            # recognize? deep learned model predict

            img_item = "/home/darknet/PycharmProjects/Python/recognition/Trainingimages/1/ul.png"
            Caught_img = "/home/darknet/PycharmProjects/Python/recognition/TestImages/ul.png"
            cv2.imwrite(Caught_img, roi_gray)
            cv2.imwrite(img_item, roi_gray)
            color = (55, 210, 55)
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



def image():
    root2 = Tk()
    root2.geometry("750x400+0+0")
    photo = PhotoImage(file="astu.png")
    thelable = Label(root2, image=photo)
    thelable.pack()
    root2.mainloop()

def ddown():
    root2 = Tk()
    root2.geometry("750x400+0+0")
    root2.title("Unlicensed Drivers Identification System")
    root2.configure(background='white')
    ddlable = Label(root2)
    ddlable.pack()
    root2.mainloop()

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="UDIS", menu=subMenu)
subMenu.add_command(label="Features", command=ddown)
subMenu.add_command(label="History ", command=ddown)
subMenu.add_command(label="About Us", command=image)
subMenu.add_separator()
subMenu.add_command(label="Others", command=ddown)

fileMenu = Menu(menu)
menu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_cascade(label="Redo", command=ddown)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_cascade(label="Redo", command=ddown)

viewMenu = Menu(menu)
menu.add_cascade(label="View", menu=viewMenu)
viewMenu.add_cascade(label="Redo", command=ddown)

windowMenu = Menu(menu)
menu.add_cascade(label="Window", menu=windowMenu)
windowMenu.add_cascade(label="Redo", command=ddown)

otherMenu = Menu(menu)
menu.add_cascade(label="Other", menu=otherMenu)
otherMenu.add_cascade(label="Redo", command=ddown)

helpMenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_cascade(label="Redo", command=ddown)


Tops = Frame(root, bg='Cadet Blue', pady=2, width=1050, height=100, relief=RIDGE)
Tops.grid(row=0, column=0)

lblTitle: Label = Label(Tops, font=('Arial', 30, 'bold'), text="Unlicensed Drivers Identification System", bd=21,
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

Platenum: Label = Label(RightFrame1, font=('Arial', 20, 'bold'), text="Vehicle-plate-number:", padx=2,pady=2, bg='Cadet Blue')
Platenum.grid(row=0, column=0, sticky=W)
txt = Entry(RightFrame1, font=('arial', 16, 'bold'), bd=2, fg="black", textvariable=platenumber, width=8, justify=LEFT).grid(row=0, column=1)


DriverId: Label = Label(RightFrame1, font=('Arial', 20, 'bold'), text="Driver-Id-number:", padx=2,pady=2, bg='Cadet Blue')
DriverId.grid(row=1, column=0, sticky=W)
txt2 = Entry(RightFrame1, font=('arial', 16, 'bold'), bd=2, fg="black", textvariable=platenumber, width=8, justify=LEFT).grid(row=1, column=1)


#root2.mainloop()
root.mainloop()








