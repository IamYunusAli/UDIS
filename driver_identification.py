import cv2

def driveridentification():
    frameWidth = 840
    frameHeight = 620
    minArea = 500
    color = (0, 0, 0)
    nPlateCascade = cv2.CascadeClassifier("resource/haarcascade_frontalface_alt2.xml")

    count = 0
    cap = cv2.VideoCapture(0)
    cap.set(3, frameWidth)
    cap.set(4, frameHeight)
    cap.set(10, 150)

    while True:
        success, img = cap.read()
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        numberPlates = nPlateCascade.detectMultiScale(imgGray, 1.1, 4)
        for(x, y, w, h) in numberPlates:
            area = w*h
            if area > minArea:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), 2)
                cv2.putText(img, "Status: Unknown",  (x+w-2, y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 1)
                cv2.putText(img, "License: Unknown", (x + w - 2, y+h-150), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 1)
                imgRoi = img[y:y+h, x:x+w]
                #cv2.imshow("ROI", imgRoi)

        cv2.imshow("", img)
        if cv2.waitKey(1) & 0xFF == ord('s'):

            cv2.imwrite("resource/Caught_Drivers/Drivers code 00"+str(count)+".jpg", imgRoi)
            cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, "Driver_captured", (150, 265), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2, (0, 0, 0), 1)
            cv2.imshow("UDIS-Driver_Recognition", img)
            cv2.waitKey(500)
            count += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

def main():
    driveridentification()
if __name__ == '__main__':
    main()






















































