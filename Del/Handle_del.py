import handle
from PyQt5.QtWidgets import QMainWindow
from Del import First_del
import about_del

class HandleWindowActions(handle.Ui_HandleWindow, QMainWindow):

    def __init__(self):

        super(handle.Ui_HandleWindow, self).__init__()
        self.use_palette()
        self.setupUi(self)
        self.push_about()
        self.setFixedSize(670, 370)

    def about_btn(self):
        self.about = about_del.aboutWindowActions()
        self.about.show()

    def push_about(self):
        self.localfile_action.triggered.connect(self.about_btn)


