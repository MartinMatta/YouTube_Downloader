from ui.MainWindow import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
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


if __name__ == '__main__' :
    app = QApplication(sys.argv)
    you_viewer_main = YoutubeDownloader()
    you_viewer_main.show()
    app.exec_()
