import typenation
from PyQt5.QtWidgets import QMainWindow
from Del import First_del
import Handle_del
from Final_del import Final
from SN_del import Song_Name
from Q_Thread import DelSong
import about_del


class AnotherWindowActions(typenation.Ui_SecondWindow, QMainWindow):

    def __init__(self):

        super(typenation.Ui_SecondWindow, self).__init__()

        self.setupUi(self)
        self.setFixedSize(670, 370)
        self.use_palette()
        self.push_about()
        self.pushButton_back.clicked.connect(self.back_btn_clicked)
        self.pushButton_next.clicked.connect(self.next_btn_clicked)
        #self.pushButton_next.clicked.connect(self.get_song_id)

    def next_page(self,msg):
        self.final_window = Final()
        self.final_window.show()
        self.handle_window.close()

    def next_btn_clicked(self):
        """
            点击相应按钮，跳转到第三个界面
        """
        if self.lineEdit_song.text() != "":
            self.thread = DelSong(self.lineEdit_song.text())
            self.thread.signal.connect(self.next_page)
            self.handle_window = Handle_del.HandleWindowActions()
            self.handle_window.show()
            self.thread.start()
            self.close()
        else:
            self.SN_window = Song_Name()
            self.SN_window.show()
            #self.label.setText("请输入歌曲名！！")
        # 实例化第三个界面的后端类，并对第三个界面进行显示


    def back_btn_clicked(self):
        """
            点击相应按钮，跳转到第一个个界面
        """
        self.another_window = First_del.FirstWindowActions()
        self.another_window.show()
        self.close()


    def change_text(self, msg):
        self.lineEdit_song.setText(str(msg))

    def about_btn(self):
        self.about = about_del.aboutWindowActions()
        self.about.show()

    def push_about(self):
        self.localfile_action.triggered.connect(self.about_btn)

