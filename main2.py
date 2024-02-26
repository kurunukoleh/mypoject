import textures
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import json
import time
ob1 = 0.001
ob2 = 0.01
ob3 = 0.1
ob4 = 1
ob5 = 2
ob6 = 3
scalepic = 128

app = QApplication([])
app.setStyleSheet("""
    QWidget {
        background-color:#111111 ;
        color : #ffffff;
        font-size: 15px;
        min-width: 1px;
        min-height : 1px;
        margin : 1 px;
    }

    QPushButton {
        background-color: #cc0000;
        color : #ffffff;
        border-radius: 5px ;
        border-color: #ff0000;
        border-style: solid;
        min-width: 100px;
        min-height: 50px;
        font-size: 15px;
        font-family: none;

    }

    QPushButton:hover {
        background-color: #ff2200;
        color : #ffffff;
        border-radius: 10px ;
        border-color: #111111;
        border-style: none;
        border-width: 10px;
        min-height: 50px;
        min-width: 100px;
        font-size: 15px;
        font-family: none;

    }


    QLineEdit {
        background-color: #111111 ;
        color : #ffffff;
        font-size: 15px;
        border-color: #000000;
        border-style: none;
        border-width: 1px;
        border-radius: 5px ;
        min-height: 30px;
    }

    QLineEdit:hover {
        background-color: #151515 ;
        color : #ffffff;
        font-size: 15px;
        border-radius: 5px ;
        border-color: #ff0000;
        border-style: solid;
        min-height: 50px;
    }


    QLabel{
        background-color: #111111 ;
        color : #ffffff;
        font-size: 15px;
        border-radius: 5px ;
        border-color: #ff0000;
        border-style: solid;
    }

    QLabel:hover{
        background-color: #111111 ;
        color : #ffffff;
        font-size: 15px;
        border-radius: 5px ;
        border-color: #000000;
        border-style: solid;
        border-width: 3px;
    }
""")
window = QWidget()
window.resize(800, 700)
mainline = QVBoxLayout()

clbtn = QPushButton("cklick")
exitbtn = QPushButton("вийти з гри")
btnshop = QPushButton('магазин')
btnbusnes = QPushButton('бізнеси')
btnback = QPushButton('міні гра')

txt = QLabel('ваші гроші :')
txt2 = QLabel('НА ХРЕСТИК НЕ НАТИСКАТИ')
txtcar = QLabel('ваша машина :')
txthouse = QLabel('ваша хата :')

with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    data["money"] += round((time.time() - data["fixtime"]) * (
                data["busnes_count1"] * ob1 + data["busnes_count2"] * ob2 + data["busnes_count3"] * ob3 + data[
            "busnes_count4"] * ob4 + data["busnes_count5"] * ob5 + data["busnes_count6"] * ob6))
    # round(data["money"])
    txt.setText(f'ваші гроші : {data["money"]}')


def exitgame():
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    data["fixtime"] = time.time()
    # data["busnes_count1"] = data2["busnes_count1"]
    # data["busnes_count2"] = data2["busnes_count2"]
    # data["busnes_count3"] = data2["busnes_count3"]
    # data["busnes_count4"] = data2["busnes_count4"]
    # data["busnes_count5"] = data2["busnes_count5"]
    # data["busnes_count6"] = data2["busnes_count6"]
    with open('data.json', 'w', ) as f:
        json.dump(data, f, indent=4)
    app.quit()


def cklick():
    data["money"] += 1
    txt.setText(f'ваші гроші : {data["money"]}')

def openbusnes1():
    if data["money"] >= 1000:
        data["money"] -= 1000
        data["busnes_count1"] += 1
        with open('data.json', 'w', ) as f:
            json.dump(data, f, indent=4)
        txt.setText(f'ваші гроші : {data["money"]}')

def openbusnes2():
    if data["money"] >= 5000:
        data["money"] -= 5000
        data["busnes_count2"] += 1
        with open('data.json', 'w', ) as f:
            json.dump(data, f, indent=4)
        txt.setText(f'ваші гроші : {data["money"]}')

def openbusnes3():
    if data["money"] >= 50000:
        data["money"] -= 50000
        data["busnes_count3"] += 1
        with open('data.json', 'w', ) as f:
            json.dump(data, f, indent=4)
        txt.setText(f'ваші гроші : {data["money"]}')

def openbusnes4():
    if data["money"] >= 1000000:
        data["money"] -= 1000000
        data["busnes_count4"] += 1
        with open('data.json', 'w', ) as f:
            json.dump(data, f, indent=4)
        txt.setText(f'ваші гроші : {data["money"]}')

def openbusnes5():
    if data["money"] >= 2000000:
        data["money"] -= 2000000
        data["busnes_count5"] += 1
        with open('data.json', 'w', ) as f:
            json.dump(data, f, indent=4)
        txt.setText(f'ваші гроші : {data["money"]}')

def openbusnes6():
    if data["money"] >= 1000000000:
        data["money"] -= 1000000000
        data["busnes_count6"] += 1
        with open('data.json', 'w', ) as f:
            json.dump(data, f, indent=4)
        txt.setText(f'ваші гроші : {data["money"]}')


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

    butonop1.clicked.connect(openbusnes1)
    butonop2.clicked.connect(openbusnes2)
    butonop3.clicked.connect(openbusnes3)
    butonop4.clicked.connect(openbusnes4)
    butonop5.clicked.connect(openbusnes5)
    butonop6.clicked.connect(openbusnes6)

    window.setLayout(mainline)
    window.show()
    window.exec()

def open_window_shop():
    with open('buttons.json', 'r', encoding='utf-8') as f:
        butons = json.load(f)
    btxt = butons['btxt']
    bubutlist = []
    shlinelist =[]
    sodbtnlist = []
    imglist = []

    window3 = QDialog()
    window3.resize(800, 600)
    mainline3 = QVBoxLayout()

    for imeger in range(15):
        imglist.append(QLabel("."))

    for bb in btxt:
        bubutlist.append(QPushButton(bb))

    for sob in range(15):
        sodbtnlist.append(QPushButton("застосувати"))

    stxtbitcoin =  QLabel('купити біткоїн')
    sbuybitcoinbtn = QPushButton('купити')
    polebuybitcoin = QLineEdit()
    ssellbitcoinbtn = QPushButton('продати')
    polesellbitcoin = QLineEdit()
    bitcoinline = QHBoxLayout()
    bitcoinline.addWidget(stxtbitcoin)
    bitcoinline.addWidget(sbuybitcoinbtn)
    bitcoinline.addWidget(polebuybitcoin)
    bitcoinline.addWidget(ssellbitcoinbtn)
    bitcoinline.addWidget(polesellbitcoin)

    for shln in range(15):
        shlinelist.append(QVBoxLayout())

    for add1 in range(15):
        shlinelist[add1].addWidget(imglist[add1])
        shlinelist[add1].addWidget(bubutlist[add1])
        shlinelist[add1].addWidget(sodbtnlist[add1])

    scarsline = QHBoxLayout()
    shousesline = QHBoxLayout()
    smambersline = QHBoxLayout()

    for it1 in range(5):
        scarsline.addLayout(shlinelist[it1])

    for it2 in range(5 , 10):
        shousesline.addLayout(shlinelist[it2])

    for it3 in range(10 , 15):
        smambersline.addLayout(shlinelist[it3])

    mainline3.addLayout(scarsline)
    mainline3.addLayout(shousesline)
    mainline3.addLayout(smambersline)
    mainline3.addLayout(bitcoinline)

    window3.setLayout(mainline3)
    window3.show()
    window3.exec()


txt.setText(f'ваші гроші : {data["money"]}')

line1 = QHBoxLayout()
line2 = QHBoxLayout()

line1.addWidget(txtcar)
line1.addWidget(txthouse)

line2.addWidget(btnshop)
line2.addWidget(btnback)
line2.addWidget(btnbusnes)

mainline.addWidget(txt2)
mainline.addWidget(exitbtn)
mainline.addLayout(line1)
mainline.addWidget(clbtn)
mainline.addWidget(txt)
mainline.addLayout(line2)

exitbtn.clicked.connect(exitgame)
clbtn.clicked.connect(cklick)
btnshop.clicked.connect(open_window_shop)
btnbusnes.clicked.connect(open_window_busnes)

window.setLayout(mainline)
window.show()
app.exec()