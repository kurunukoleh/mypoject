import textures
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
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
    window3 = QDialog()
    window3.resize(800, 600)
    mainline3 = QVBoxLayout()

    simeger1 = QLabel('.')
    simeger2 = QLabel('.')
    simeger3 = QLabel('.')
    simeger4 = QLabel('.')
    simeger5 = QLabel('.')
    simeger6 = QLabel('.')
    simeger7 = QLabel('.')
    simeger8 = QLabel('.')
    simeger9 = QLabel('.')
    simeger10 = QLabel('.')
    simeger11 = QLabel('.')
    simeger12 = QLabel('.')
    simeger13 = QLabel('.')
    simeger14 = QLabel('.')
    simeger15 = QLabel('.')

    sbbtn1 = QPushButton('купити : ')
    sbbtn2 = QPushButton('купити : ')
    sbbtn3 = QPushButton('купити : ')
    sbbtn4 = QPushButton('купити : ')
    sbbtn5 = QPushButton('купити : ')
    sbbtn6 = QPushButton('купити : ')
    sbbtn7 = QPushButton('купити : ')
    sbbtn8 = QPushButton('купити : ')
    sbbtn9 = QPushButton('купити : ')
    sbbtn10 = QPushButton('купити : ')
    sbbtn11 = QPushButton('купити : ')
    sbbtn12 = QPushButton('купити : ')
    sbbtn13 = QPushButton('купити : ')
    sbbtn14 = QPushButton('купити : ')
    sbbtn15 = QPushButton('купити : ')

    sodbtn1 = QPushButton('застосувати :')
    sodbtn2 = QPushButton('застосувати :')
    sodbtn3 = QPushButton('застосувати :')
    sodbtn4 = QPushButton('застосувати :')
    sodbtn5 = QPushButton('застосувати :')
    sodbtn6 = QPushButton('застосувати :')
    sodbtn7 = QPushButton('застосувати :')
    sodbtn8 = QPushButton('застосувати :')
    sodbtn9 = QPushButton('застосувати :')
    sodbtn10 = QPushButton('застосувати :')
    sodbtn11 = QPushButton('застосувати :')
    sodbtn12 = QPushButton('застосувати :')
    sodbtn13 = QPushButton('застосувати :')
    sodbtn14 = QPushButton('застосувати :')
    sodbtn15 = QPushButton('застосувати :')
    sodbtn16 = QPushButton('застосувати :')

    sodbtn1.hide()
    sodbtn2.hide()
    sodbtn3.hide()
    sodbtn4.hide()
    sodbtn5.hide()
    sodbtn6.hide()
    sodbtn7.hide()
    sodbtn8.hide()
    sodbtn9.hide()
    sodbtn10.hide()
    sodbtn11.hide()
    sodbtn12.hide()
    sodbtn13.hide()
    sodbtn14.hide()
    sodbtn15.hide()

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

    shline1 = QVBoxLayout()
    shline2 = QVBoxLayout()
    shline3 = QVBoxLayout()
    shline4 = QVBoxLayout()
    shline5 = QVBoxLayout()
    shline6 = QVBoxLayout()
    shline7 = QVBoxLayout()
    shline8 = QVBoxLayout()
    shline9 = QVBoxLayout()
    shline10 = QVBoxLayout()
    shline11 = QVBoxLayout()
    shline12 = QVBoxLayout()
    shline13 = QVBoxLayout()
    shline14 = QVBoxLayout()
    shline15 = QVBoxLayout()


    shline1.addWidget(simeger1)
    shline1.addWidget(sbbtn1)
    shline1.addWidget(sodbtn1)

    shline2.addWidget(simeger2)
    shline2.addWidget(sbbtn2)
    shline2.addWidget(sodbtn2)

    shline3.addWidget(simeger3)
    shline3.addWidget(sbbtn3)
    shline3.addWidget(sodbtn3)

    shline4.addWidget(simeger4)
    shline4.addWidget(sbbtn4)
    shline4.addWidget(sodbtn4)

    shline5.addWidget(simeger5)
    shline5.addWidget(sbbtn5)
    shline5.addWidget(sodbtn5)

    shline6.addWidget(simeger6)
    shline6.addWidget(sbbtn6)
    shline6.addWidget(sodbtn6)

    shline7.addWidget(simeger7)
    shline7.addWidget(sbbtn7)
    shline7.addWidget(sodbtn7)

    shline8.addWidget(simeger8)
    shline8.addWidget(sbbtn8)
    shline8.addWidget(sodbtn8)

    shline9.addWidget(simeger9)
    shline9.addWidget(sbbtn9)
    shline9.addWidget(sodbtn9)

    shline10.addWidget(simeger10)
    shline10.addWidget(sbbtn10)
    shline10.addWidget(sodbtn10)

    shline11.addWidget(simeger11)
    shline11.addWidget(sbbtn11)
    shline11.addWidget(sodbtn11)

    shline12.addWidget(simeger12)
    shline12.addWidget(sbbtn12)
    shline12.addWidget(sodbtn12)

    shline13.addWidget(simeger13)
    shline13.addWidget(sbbtn13)
    shline13.addWidget(sodbtn13)

    shline14.addWidget(simeger14)
    shline14.addWidget(sbbtn14)
    shline14.addWidget(sodbtn14)

    shline15.addWidget(simeger15)
    shline15.addWidget(sbbtn15)
    shline15.addWidget(sodbtn15)

    scarsline = QHBoxLayout()
    shousesline = QHBoxLayout()
    smambersline = QHBoxLayout()

    scarsline.addLayout(shline1)
    scarsline.addLayout(shline2)
    scarsline.addLayout(shline3)
    scarsline.addLayout(shline4)
    scarsline.addLayout(shline5)

    shousesline.addLayout(shline6)
    shousesline.addLayout(shline7)
    shousesline.addLayout(shline8)
    shousesline.addLayout(shline9)
    shousesline.addLayout(shline10)

    smambersline.addLayout(shline11)
    smambersline.addLayout(shline12)
    smambersline.addLayout(shline13)
    smambersline.addLayout(shline14)
    smambersline.addLayout(shline15)

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