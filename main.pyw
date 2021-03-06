from ui.MainWindow import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import uic
import subprocess
import pytube
import sys
import os
import re


class YoutubeDownloader(QMainWindow, Ui_MainWindow) :
    def __init__(self) :
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle('Youtube Downloader')
        self.setWindowIcon(
            QtGui.QIcon(
                "D:/YouTube_Downloader/ui\\../resource/youtube.png"
            )
        )

        self.save_path = "./"
        self.initUI()
        

    @pyqtSlot()
    def on_click_download(self):
        format_ = self.comboBox.currentText()
        url = self.lineEdit.text()

        if format_ == "mp3":
            print(url)
        elif format_ == "mp4":
            self.download(url)


    @pyqtSlot()
    def on_click_browse(self):
        self.save_path = QFileDialog.getExistingDirectory(
            self, 'Select the Directory'
        )
        self.lineEdit_2.setText(self.save_path)
       

    def initUI(self):
        self.pushButton.clicked.connect(self.on_click_browse)
        self.pushButton_2.clicked.connect(self.on_click_download)

        self.lineEdit_2.setText(self.save_path)

    def download(self, url):
        youtube = pytube.YouTube(url)
        video = youtube.streams.get_highest_resolution()
        video.download(self.save_path)


if __name__ == '__main__' :
    app = QApplication(sys.argv)
    you_viewer_main = YoutubeDownloader()
    you_viewer_main.show()
    app.exec_()
