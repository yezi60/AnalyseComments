import sys
import destination
from Del import Second_del
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
import about_del

# 注意这里定义的第一个界面的后端代码类需要继承两个类
class FirstWindowActions(destination.Ui_MainWindow, QMainWindow):

    def __init__(self):

        super(destination.Ui_MainWindow, self).__init__()
        # 设置颜色
        self.use_palette()
        # 创建界面
        self.setupUi(self)
        #不可调整大小
        self.setFixedSize(670, 370)
        self.push_about()
        self.pushButton_start.clicked.connect(self.start_btn_clicked)
        self.pushButton_exit.clicked.connect(self.close_btn_clicked)

    def start_btn_clicked(self):
        """
            点击相应按钮，跳转到第二个界面
        """
        # 实例化第二个界面的后端类，并对第二个界面进行显示
        self.another_window = Second_del.AnotherWindowActions()
        self.another_window.show()
        self.close()

    def close_btn_clicked(self):
        """
            点击相应按钮，关闭界面
        """
        self.close()

    def about_btn(self):
        self.about = about_del.aboutWindowActions()
        self.about.show()

    def push_about(self):
        self.localfile_action.triggered.connect(self.about_btn)

if __name__ == '__main__':

    # 这里是界面的入口，在这里需要定义QApplication对象，之后界面跳转时不用再重新定义，只需要调用show()函数即可
    app = QApplication(sys.argv)

    # 显示创建的界面
    demo_window = FirstWindowActions()
    demo_window.show()

    sys.exit(app.exec_())
