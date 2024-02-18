from setings import data
import funkcias
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import json
import textures
#from main import data

with open('data.json', 'r', encoding='utf-8') as f:
    data2 = json.load(f)

scalepic = 128

def open_window_busnes():
    window = QDialog()
    window.resize(800, 600)
    mainline = QVBoxLayout()

    img1 = QPixmap(textures.busnes_texture1)
    img2 = QPixmap(textures.busnes_texture2)
    img3 = QPixmap(textures.busnes_texture3)
    img4 = QPixmap(textures.busnes_texture4)
    img5 = QPixmap(textures.busnes_texture5)
    img6 = QPixmap(textures.busnes_texture6)

    img1 = img1.scaled(scalepic , scalepic)
    img2 = img2.scaled(scalepic, scalepic)
    img3 = img3.scaled(scalepic, scalepic)
    img4 = img4.scaled(scalepic, scalepic)
    img5 = img5.scaled(scalepic, scalepic)
    img6 = img6.scaled(scalepic, scalepic)

    imeger1 = QLabel(".")
    imeger2 = QLabel(".")
    imeger3 = QLabel(".")
    imeger4 = QLabel(".")
    imeger5 = QLabel(".")
    imeger6 = QLabel(".")

    imeger1.setPixmap(img1)
    imeger2.setPixmap(img2)
    imeger3.setPixmap(img3)
    imeger4.setPixmap(img4)
    imeger5.setPixmap(img5)
    imeger6.setPixmap(img6)

    butonop1 = QPushButton("відкрити бізнес : шаурма")
    butonop2 = QPushButton("відкрити бізнес : СТО")
    butonop3 = QPushButton("відкрити бізнес : маркет")
    butonop4 = QPushButton("відкрити бізнес : завод")
    butonop5 = QPushButton("відкрити бізнес : програмне забезпечення")
    butonop6 = QPushButton("відкрити бізнес : холдингова компанія")

    txt1 = QLabel(f'відкрито : {data["busnes_count1"]}')
    txt2 = QLabel(f'відкрито : {data["busnes_count2"]}')
    txt3 = QLabel(f'відкрито : {data["busnes_count3"]}')
    txt4 = QLabel(f'відкрито : {data["busnes_count4"]}')
    txt5 = QLabel(f'відкрито : {data["busnes_count5"]}')
    txt6 = QLabel(f'відкрито : {data["busnes_count6"]}')

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

    #txt1.hide()
    #txt2.hide()
    #txt3.hide()
    #txt4.hide()
    #txt5.hide()
    #txt6.hide()

    butonop1.clicked.connect(funkcias.openbusnes1)
    butonop2.clicked.connect(funkcias.openbusnes2)
    butonop3.clicked.connect(funkcias.openbusnes3)
    butonop4.clicked.connect(funkcias.openbusnes4)
    butonop5.clicked.connect(funkcias.openbusnes5)
    butonop6.clicked.connect(funkcias.openbusnes6)

    window.setLayout(mainline)
    window.show()
    window.exec()
