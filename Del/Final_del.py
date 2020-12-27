import final
import about_del
from Del import First_del
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PIL import Image
from PyQt5.QtCore import Qt, QThread, pyqtSignal

class Final(final.Final_Window, QMainWindow):

    def __init__(self):

        super(final.Final_Window, self).__init__()
        self.setupUi(self)
        self.use_palette()
        self.setFixedSize(300, 200)

        self.open_Button.clicked.connect(self.open_btn_clicked)
        self.back_Button.clicked.connect(self.back_btn_clicked)


    def open_btn_clicked(self):
        self.thread = DelPic()
        self.thread.start()
        #self.close()



    def back_btn_clicked(self):
        """
            点击相应按钮，跳转到第一个个界面
        """
        self.another_window = First_del.FirstWindowActions()
        self.another_window.show()
        self.close()

    def about_btn(self):
        self.about = about_del.aboutWindowActions()
        self.about.show()


class DelPic(QThread):
    """该线程用于计算耗时的累加操作"""
    #_song = pyqtSignal(str)  # 信号类型 str

    def __init__(self):
        super().__init__()


    def run(self):
        dir_pic = "E:\\PycharmProjects\\Pybasic\\Del\\word_cloud.png"
        img = Image.open(dir_pic)
        img.show()