
import Final_del
from Spicies.Spicy import run_spicy
from PyQt5.QtCore import Qt, QThread, pyqtSignal


class DelSong(QThread):
    """该线程用于计算耗时的累加操作"""
    signal = pyqtSignal(str)  # 信号类型 str

    def __init__(self, song):
        super().__init__()
        self.song = song


    def run(self):
        print("run")
        run_spicy(str(self.song))
        dir_pic = "E:\\PycharmProjects\\Pybasic\\Del\\word_cloud.png"
        print("s")
        # fin_win = Final_Dialog()
        # fin_win.show()
        self.signal.emit(str("正在处理"))