import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication
from Final_del import Final
import final

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Final()
    widget.show()
    sys.exit(app.exec_())


