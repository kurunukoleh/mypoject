from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import json

def open_window_shop():
    window = QDialog()
    window.resize(800, 600)
    mainline = QVBoxLayout()

    a = QLabel('g')
    mainline.addWidget(a)

    window.setLayout(mainline)
    window.show()
    window.exec()