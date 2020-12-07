from PyQt5 import QtWidgets
from PyQt5 import QtCore
import sys
#from PyQt5.QtWidgets import QLabel, QLineEdit

class MyWindows(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("파이썬GUI")

        label1 = QtWidgets.QLabel("라벨1 입니다.", self)
        label1.setAlignment(QtCore.Qt.AlignCenter)
        label1.resize(60, 25)

        label2 = QtWidgets.QLabel("라벨2 입니다.", self)
        label2.setAlignment(QtCore.Qt.AlignRight)
        label2.setStyleSheet("color:red; font-size:20px;")

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(label2)

        self.setLayout(layout)
        self.show()

app = QtWidgets.QApplication([])
win = MyWindows()
sys.exit(app.exec_())


