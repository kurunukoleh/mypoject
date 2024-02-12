
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import json

def open_window_busnes():
    window = QDialog()
    window.resize(800, 600)
    mainline = QVBoxLayout()

    imeger1 = QLabel(".")
    imeger2 = QLabel(".")
    imeger3 = QLabel(".")
    imeger4 = QLabel(".")
    imeger5 = QLabel(".")
    imeger6 = QLabel(".")

    butonop1 = QPushButton(".")
    butonop2 = QPushButton(".")
    butonop3 = QPushButton(".")
    butonop4 = QPushButton(".")
    butonop5 = QPushButton(".")
    butonop6 = QPushButton(".")

    txt1 = QLabel(".")
    txt2 = QLabel(".")
    txt3 = QLabel(".")
    txt4 = QLabel(".")
    txt5 = QLabel(".")
    txt6 = QLabel(".")

    line1 = QVBoxLayout()
    line2 = QVBoxLayout()
    line3 = QVBoxLayout()
    line4 = QVBoxLayout()
    line5 = QVBoxLayout()
    line6 = QVBoxLayout()

    line1.addWidget(imeger1)
    line1.addWidget(butonop1)
    line1.addWidget(txt1)
    line2.addWidget(imeger2)
    line2.addWidget(butonop2)
    line2.addWidget(txt2)
    line3.addWidget(imeger3)
    line3.addWidget(butonop3)
    line3.addWidget(txt3)
    line4.addWidget(imeger4)
    line4.addWidget(butonop4)
    line4.addWidget(txt4)
    line5.addWidget(imeger5)
    line5.addWidget(butonop5)
    line5.addWidget(txt5)
    line6.addWidget(imeger6)
    line6.addWidget(butonop6)
    line6.addWidget(txt6)

    ln1 = QHBoxLayout()
    ln2 = QHBoxLayout()

    ln1.addLayout(line1)
    ln1.addLayout(line2)
    ln1.addLayout(line3)
    ln2.addLayout(line4)
    ln2.addLayout(line5)
    ln2.addLayout(line6)

    mainline.addLayout(ln1)
    mainline.addLayout(ln2)

    txt1.hide()
    txt2.hide()
    txt3.hide()
    txt4.hide()
    txt5.hide()
    txt6.hide()

    window.setLayout(mainline)
    window.show()
    window.exec()
