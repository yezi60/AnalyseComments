import handle
from PyQt5.QtWidgets import QMainWindow
import about


class aboutWindowActions(about.About_MainWindow, QMainWindow):

    def __init__(self):
        super(about.About_MainWindow, self).__init__()
        #self.use_palette()
        self.setupUi(self)
        self.setFixedSize(670, 370)

