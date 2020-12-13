import cv2
import os
import numpy as np
import pickle
def capture():

    minArea = 500
    color = (0, 0, 0)
    count = 0
    lablels = {"person_name":1}
    frameWidth = 940
    frameHeight = 520
    face_cascade = cv2.CascadeClassifier(r'C:\Users\Yunus\Desktop\UDIS\resource\haarcascade_frontalface_alt2.xml')
    fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
    vid = cv2.VideoWriter(r'C:\Users\Yunus\Desktop\UDIS\resource\Recording\video.mp4',fourcc,25,(640,480))
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("Trainned_drivers_face.yml")

    with open(r"C:\Users\Yunus\Desktop\UDIS\labels.pickle", 'rb') as f:
        og_lablels = pickle.load(f)
        print(og_lablels.items())
        lablels = {v:k for k,v in og_lablels.items()}

    cap = cv2.VideoCapture(0)
    cap.set(3, frameWidth)
    cap.set(4, frameHeight)
    cap.set(10, 150)

    while True:
        # Capture frame-by-frame
        img, dface = cap.read()
        ####record

        img_gray = cv2.cvtColor(dface, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(img_gray, scaleFactor=1.1, minNeighbors=4)

        for (x, y, w, h) in faces:
            print(x, y, w, h)
            roi_gray = img_gray[y:y + h, x:x + w]
            roi_color = dface[y:y + h, x:x + w]


            id_, conf = recognizer.predict(roi_gray)
            if conf >= 45:
                print(id_)
                print(lablels[id_])
                area = w * h
                #if id_ == 1:

                cv2.putText(dface, lablels[id_], (x + w - 2, y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 1)
                #Caught_image = "/home/darknet/PycharmProjects/Python/resource/Caught_Drivers/Caught_driver1.png"
                #cv2.imwrite(Caught_image, roi_gray)
                vid.write(dface)
                if area > minArea:
                    cv2.rectangle(dface, (x, y), (x + w, y + h), (0, 0, 0), 2)
                    cv2.putText(dface, lablels[id_], (x + w - 2, y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 1)


            ##save some captured images
            #img_item = "/home/darknet/PycharmProjects/Python/recognition/Trainingimages/0/ul.png"
            #cv2.imwrite(img_item, roi_gray)

            ## draw a rectangle around the face
            #color = (55, 250, 55)
            #stroke = 2
            #horizontal_len = x + w + 5
            #vertical_len = y + h + 5
            #cv2.rectangle(dface, (x, y), (horizontal_len, vertical_len), color, stroke)

            cv2.rectangle(dface, (x, y), (x + w, y + h), (0, 0, 0), 2)

        # display the resulting frame
        cv2.imshow('UDIS-Drivers-Identification ', dface)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    # when everything is done, release the captureqssE
    cap.release()
    cv2.destroyAllWindows()

capture()