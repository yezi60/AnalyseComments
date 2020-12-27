import song_name

from Del import First_del
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

from PyQt5.QtCore import Qt, QThread, pyqtSignal

class Song_Name(song_name.Song_Window, QMainWindow):

    def __init__(self):

        super(song_name.Song_Window, self).__init__()
        self.setupUi(self)
        #self.use_palette()
        self.setFixedSize(360, 200)

        self.close_Button.clicked.connect(self.close)










