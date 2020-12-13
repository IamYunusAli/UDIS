import sys
from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets
from PySide2.QtMultimedia import QMediaPlayer, QMediaPlaylist
from PySide2.QtCore import QUrl
from PySide2.QtMultimediaWidgets import QVideoWidget


class VideoPlayer(QtWidgets.QWidget):
    def __init__(self):
        super(VideoPlayer, self).__init__()
        self.player = QMediaPlayer()
        self.resize(QtCore.QSize(400, 300))
        self.playlist = QMediaPlaylist(self.player)
        self.playlist.addMedia(QUrl(u"resource\Recording\Instagram.mp4"))
        self.video_widget = QVideoWidget()
        self.player.setVideoOutput(self.video_widget)
        self.playlist.setCurrentIndex(0)
        self.player.setPlaylist(self.playlist)
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.video_widget)
        self.setLayout(self.layout)
        self.player.play()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    player = VideoPlayer()
    player.raise_()
    player.show()
    app.exec_()
