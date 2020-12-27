from PyQt5 import QtWidgets
import sys
from destination import Ui_MainWindow
from typenation import Ui_SecondWindow


class Realize_Ui_MainWindow(Ui_MainWindow):

    def setupFunction(self):
        #self.pushButton_start.clicked.connect(Ui_SecondWindow.show)
        self.pushButton_exit.clicked.connect(exit)

    def exit1(self):
        print("exit")




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # 创建一个QApplication，也就是你要开发的软件app
    MainWindow = QtWidgets.QMainWindow()    # 创建一个QMainWindow，用来装载你需要的各种组件、控件
    #ui = Realize_Ui_MainWindow()            # ui是父类Ui_MainWindow()类的实例化对象
    ui = Ui_SecondWindow()
    ui.setupUi(MainWindow)                  # 执行类中的setupUi方法，方法的参数是第二步中创建的QMainWindow
    #ui.setupFunction()
    MainWindow.show()                       # 执行QMainWindow的show()方法，显示这个QMainWindow
    sys.exit(app.exec_())                   # 使用exit()或者点击关闭按钮退出QApplication