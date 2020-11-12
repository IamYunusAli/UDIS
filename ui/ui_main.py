from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"background-color: rgb(56, 58, 89);	\n"
"	color: rgb(220, 220, 220);\n"
"	border-radius: 10px;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.mainframe = QFrame(self.centralwidget)
        self.mainframe.setObjectName(u"mainframe")
        self.mainframe.setFrameShape(QFrame.StyledPanel)
        self.mainframe.setFrameShadow(QFrame.Raised)
        self.screen = QLabel(self.mainframe)
        self.screen.setObjectName(u"screen")
        self.screen.setGeometry(QRect(-10, -10, 800, 600))
        font = QFont()
        font.setFamily(u"Segoe UI Semibold")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.screen.setFont(font)
        self.screen.setStyleSheet(u"QFrame {	\n"
"	background-color: rgb(56, 58, 89);	\n"
"	color: rgb(220, 220, 220);\n"
"}")
        self.screen.setAlignment(Qt.AlignCenter)
        self.pushButton = QPushButton(self.mainframe)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(50, 530, 131, 41))
        font1 = QFont()
        font1.setFamily(u"Segoe UI Semibold")
        font1.setPointSize(19)
        font1.setBold(True)
        font1.setWeight(75)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"background-color: rgba(93, 179, 100);")
        self.pushButton_2 = QPushButton(self.mainframe)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(250, 530, 121, 41))
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setStyleSheet(u"background-color: rgba(163, 65, 65);")

        self.verticalLayout.addWidget(self.mainframe)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.screen.setText(QCoreApplication.translate("MainWindow", u"UDIS", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
    # retranslateUi

