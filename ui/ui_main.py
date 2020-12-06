import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import cv2


class Ui_MainWindow(object):

    def driverId(self):
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
            for (x, y, w, h) in numberPlates:
                area = w * h
                if area > minArea:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), 2)
                    cv2.putText(img, "Status: Unknown", (x + w - 2, y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 1)
                    cv2.putText(img, "License: Unknown", (x + w - 2, y + h - 150), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1,
                                color, 1)
                    imgRoi = img[y:y + h, x:x + w]
                    cv2.imshow("ROI", imgRoi)

            cv2.imshow("", img)
            if cv2.waitKey(1) & 0xFF == ord('s'):
                cv2.imwrite("resource/Caught_Drivers/Drivers code 00" + str(count) + ".jpg", imgRoi)
                cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, "Driver_captured", (150, 265), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2, (0, 0, 0), 1)
                cv2.imshow("UDIS-Driver_Recognition", img)
                cv2.waitKey(500)
                count += 1
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    def closeme(self):
        sys.exit()
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"background-color: rgb(56, 58, 89);	\n""	color: rgb(220, 220, 220);\n""	border-radius: 10px;")

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.mainframe = QFrame(self.centralwidget)
        self.mainframe.setObjectName(u"mainframe")
        self.mainframe.setFrameShape(QFrame.StyledPanel)
        self.mainframe.setFrameShadow(QFrame.Raised)

        self.pushButton = QPushButton(self.mainframe)
        self.pushButton.setObjectName(u"pushButton")
       ## self.pushButton.clicked.connect(self.driverId())
        self.pushButton.setGeometry(QRect(150, 530, 91, 31))
        font = QFont()
        font.setFamily(u"Segoe UI Semibold")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"background-color: rgba(93, 179, 100);\n""shadow: rgb(220,230,221)")
        self.pushButton_2 = QPushButton(self.mainframe)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(270, 530, 91, 31))
        font1 = QFont()
        font1.setFamily(u"Segoe UI Semibold")
        font1.setPointSize(15)
        font1.setBold(True)
        font1.setWeight(75)
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setStyleSheet(u"background-color: rgba(163, 65, 65);")
        self.pushButton_2.setFlat(False)
        self.videowindow = QFrame(self.mainframe)
        self.videowindow.setObjectName(u"videowindow")
        self.videowindow.setGeometry(QRect(10, 40, 581, 471))
        self.videowindow.setStyleSheet(u"background-color: rgb(52, 59, 72\n""\n"");\n""")
        self.videowindow.setFrameShape(QFrame.StyledPanel)
        self.videowindow.setFrameShadow(QFrame.Raised)
        self.widget = QWidget(self.videowindow)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 581, 471))
        self.caughtpic = QFrame(self.mainframe)
        self.caughtpic.setObjectName(u"caughtpic")
        self.caughtpic.setGeometry(QRect(600, 40, 171, 191))
        self.caughtpic.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.caughtpic.setFrameShape(QFrame.StyledPanel)
        self.caughtpic.setFrameShadow(QFrame.Raised)
        self.caughtlicense = QFrame(self.mainframe)
        self.caughtlicense.setObjectName(u"caughtlicense")
        self.caughtlicense.setGeometry(QRect(600, 320, 171, 41))
        self.caughtlicense.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.caughtlicense.setFrameShape(QFrame.StyledPanel)
        self.caughtlicense.setFrameShadow(QFrame.Raised)
        self.titlebar = QFrame(self.mainframe)
        self.titlebar.setObjectName(u"titlebar")
        self.titlebar.setGeometry(QRect(0, 0, 621, 31))
        self.titlebar.setFrameShape(QFrame.StyledPanel)
        self.titlebar.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.titlebar)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 0, 51, 31))
        font2 = QFont()
        font2.setFamily(u"A0 Addis Abeba Unicode")
        font2.setPointSize(16)
        font2.setBold(True)
        font2.setWeight(75)
        self.label.setFont(font2)
        self.label_4 = QLabel(self.titlebar)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(80, 5, 351, 21))
        font3 = QFont()
        font3.setPointSize(14)
        self.label_4.setFont(font3)
        self.label_2 = QLabel(self.mainframe)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(620, 240, 141, 31))
        font4 = QFont()
        font4.setPointSize(14)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_2.setFont(font4)
        self.label_3 = QLabel(self.mainframe)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(620, 380, 141, 31))
        font5 = QFont()
        font5.setPointSize(15)
        font5.setBold(True)
        font5.setWeight(75)
        self.label_3.setFont(font5)
        self.dateTimeEdit = QDateTimeEdit(self.mainframe)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setGeometry(QRect(590, 540, 194, 31))
        font6 = QFont()
        font6.setPointSize(10)
        self.dateTimeEdit.setFont(font6)
        self.btn_maximize = QPushButton(self.mainframe)
        self.btn_maximize.setObjectName(u"btn_Maximize")
        self.btn_maximize.setGeometry(QRect(690, 10, 16, 16))
        self.btn_maximize.setMinimumSize(QSize(15, 15))
        self.btn_maximize.setMaximumSize(QSize(17, 17))
        self.btn_maximize.setStyleSheet(u"QPushButton{\n""border: none;\n""border-radius: 8px;\n""background-color:rgb(85,255,127)\n""}\n""QPushButton:hover{\n""background-color: rgba(85, 255, 127, 150);\n""}\n""")

        self.btn_minimize = QPushButton(self.mainframe)
        self.btn_minimize.setObjectName(u"btn_MInimize")
        self.btn_minimize.setGeometry(QRect(720, 10, 16, 16))
        #self.btn_minimize.clicked.connetct(self.min)
        self.btn_minimize.setMinimumSize(QSize(15, 15))
        self.btn_minimize.setMaximumSize(QSize(17, 17))
        self.btn_minimize.setStyleSheet(u"QPushButton{\n""border: none;\n""border-radius: 8px;\n""background-color:rgb(255,170,0)\n""}\n""QPushButton:hover{\n""	background-color: rgba(255, 170, 0, 150);\n""}\n""")

        self.btn_close = QPushButton(self.mainframe)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.clicked.connect(self.closeme)
        self.btn_close.setGeometry(QRect(750, 10, 16, 16))
        self.btn_close.setMinimumSize(QSize(15, 15))
        self.btn_close.setMaximumSize(QSize(17, 17))
        self.btn_close.setStyleSheet(u"QPushButton{\n""border: none;\n""border-radius: 8px;\n""	background-color: rgb(255, 0, 0);\n""}\n""QPushButton:hover{\n""background-color: rgba(255, 0, 0, 150);\n""}\n""")

        self.verticalLayout.addWidget(self.mainframe)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"UDIS", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"(Unlicense Drivers Identification system)", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Caught Driver", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"License Plate", None))
#if QT_CONFIG(tooltip)
        self.btn_maximize.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
    # retranslateUi




