import textures
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import json
import time
import requests

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
        background-color: #333333 ;
        color : #ffffff;
        font-size: 15px;
        border-color: #000000;
        border-style: none;
        border-width: 1px;
        border-radius: 5px ;
        min-height: 30px;
    }

    QLineEdit:hover {
        background-color: #444444 ;
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
txtmamber = QLabel('ваш предмет :')

with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

data["money"] += round((time.time() - data["fixtime"]) * (data["busnes_count1"] * ob1 + data["busnes_count2"] * ob2 + data["busnes_count3"] * ob3 + data["busnes_count4"] * ob4 + data["busnes_count5"] * ob5 + data["busnes_count6"] * ob6))
# round(data["money"])
txt.setText(f'ваші гроші : {data["money"]}')
try:
    txtcar.setPixmap(QPixmap(data['thiscar']).scaled(128,128))
except:
    txtcar.setText('ваша машина :')

try:
    txthouse.setPixmap(QPixmap(data['thishouse']).scaled(128,128))
except:
    txtcar.setText('ваша машина :')

try:
    txtmamber.setPixmap(QPixmap(data['thismember']).scaled(128,128))
except:
    txtcar.setText('ваша машина :')


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
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    with open('buttons.json', 'r', encoding='utf-8') as f:
        butons = json.load(f)
    btxt = butons['btxt']
    imgtxt = butons['imgtxt']
    bubutlist = []
    shlinelist =[]
    sodbtnlist = []
    imglist = []
    pixmaplist = []

    window3 = QDialog()
    window3.resize(1200, 800)
    mainline3 = QVBoxLayout()

    for img in imgtxt:
        pixmaplist.append(QPixmap(img).scaled(128 , 128))

    for imeger in range(15):
        imglist.append(QLabel("."))

    for setim in range(15):
        imglist[setim].setPixmap(pixmaplist[setim])

    for bb in btxt:
        bubutlist.append(QPushButton(bb))

    for sob in range(15):
        sodbtnlist.append(QPushButton("застосувати"))

    for sob2 in sodbtnlist:
        sob2.hide()

    for sh in range(15):
        if data['buylist'][sh] == 1:
            sodbtnlist[sh].show()

    stxtbitcoin =  QLabel('купити біткоїн')
    sbuybitcoinbtn = QPushButton('купити')
    polebuybitcoin = QLineEdit()
    ssellbitcoinbtn = QPushButton('продати')
    polesellbitcoin = QLineEdit()
    sbitcointxt = QLabel(f'біткойнів у вас : {data["bitcoincount"]}')
    bitcoinline = QHBoxLayout()
    bitcoinline.addWidget(stxtbitcoin)
    bitcoinline.addWidget(sbuybitcoinbtn)
    bitcoinline.addWidget(polebuybitcoin)
    bitcoinline.addWidget(ssellbitcoinbtn)
    bitcoinline.addWidget(polesellbitcoin)
    bitcoinline.addWidget(sbitcointxt)

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

    def buy1():
        global data
        if data['money'] >= 3000:
            data['money'] -= 3000
            data['buylist'][0] = 1
            sodbtnlist[0].show()
            with open('data.json', 'w', ) as f:
                json.dump(data, f, indent=4)
            global txt
            txt.setText(f'ваші гроші : {data["money"]}')

    def buy2():
        global data
        if data['money'] >= 6000:
            data['money'] -= 6000
            data['buylist'][1] = 1
            sodbtnlist[1].show()
            with open('data.json', 'w', ) as f:
                json.dump(data, f, indent=4)
            global txt
            txt.setText(f'ваші гроші : {data["money"]}')

    def buy3():
        global data
        if data['money'] >= 50000:
            data['money'] -= 50000
            data['buylist'][2] = 1
            sodbtnlist[2].show()
            with open('data.json', 'w', ) as f:
                json.dump(data, f, indent=4)
            global txt
            txt.setText(f'ваші гроші : {data["money"]}')

    def buy4():
        global data
        if data['money'] >= 300000:
            data['money'] -= 300000
            data['buylist'][3] = 1
            sodbtnlist[3].show()
            with open('data.json', 'w', ) as f:
                json.dump(data, f, indent=4)
            global txt
            txt.setText(f'ваші гроші : {data["money"]}')

    def buy5():
        global data
        if data['money'] >= 5000000:
            data['money'] -= 5000000
            data['buylist'][4] = 1
            sodbtnlist[4].show()
            with open('data.json', 'w', ) as f:
                json.dump(data, f, indent=4)
            global txt
            txt.setText(f'ваші гроші : {data["money"]}')

    def buy6():
        global data
        if data['money'] >= 20000:
            data['money'] -= 20000
            data['buylist'][5] = 1
            sodbtnlist[5].show()
            with open('data.json', 'w', ) as f:
                json.dump(data, f, indent=4)
            global txt
            txt.setText(f'ваші гроші : {data["money"]}')

    def buy7():
        global data
        if data['money'] >= 50000:
            data['money'] -= 50000
            data['buylist'][6] = 1
            sodbtnlist[6].show()
            with open('data.json', 'w', ) as f:
                json.dump(data, f, indent=4)
            global txt
            txt.setText(f'ваші гроші : {data["money"]}')

    def buy8():
        global data
        if data['money'] >= 100000:
            data['money'] -= 100000
            data['buylist'][7] = 1
            sodbtnlist[7].show()
            with open('data.json', 'w', ) as f:
                json.dump(data, f, indent=4)
            global txt
            txt.setText(f'ваші гроші : {data["money"]}')

    def buy9():
        global data
        if data['money'] >= 500000000:
            data['money'] -= 500000000
            data['buylist'][8] = 1
            sodbtnlist[8].show()
            with open('data.json', 'w', ) as f:
                json.dump(data, f, indent=4)
            global txt
            txt.setText(f'ваші гроші : {data["money"]}')

    def buy10():
        global data
        if data['money'] >= 1000000000:
            data['money'] -= 1000000000
            data['buylist'][9] = 1
            sodbtnlist[9].show()
            with open('data.json', 'w', ) as f:
                json.dump(data, f, indent=4)
            global txt
            txt.setText(f'ваші гроші : {data["money"]}')

    def buy11():
        global data
        if data['money'] >= 5000:
            data['money'] -= 5000
            data['buylist'][10] = 1
            sodbtnlist[10].show()
            with open('data.json', 'w', ) as f:
                json.dump(data, f, indent=4)
            global txt
            txt.setText(f'ваші гроші : {data["money"]}')

    def buy12():
        global data
        if data['money'] >= 30000:
            data['money'] -= 30000
            data['buylist'][11] = 1
            sodbtnlist[11].show()
            with open('data.json', 'w', ) as f:
                json.dump(data, f, indent=4)
            global txt
            txt.setText(f'ваші гроші : {data["money"]}')

    def buy13():
        global data
        if data['money'] >= 3000000:
            data['money'] -= 3000000
            data['buylist'][12] = 1
            sodbtnlist[12].show()
            with open('data.json', 'w', ) as f:
                json.dump(data, f, indent=4)
            global txt
            txt.setText(f'ваші гроші : {data["money"]}')

    def buy14():
        global data
        if data['money'] >= 20000000:
            data['money'] -= 20000000
            data['buylist'][13] = 1
            sodbtnlist[13].show()
            with open('data.json', 'w', ) as f:
                json.dump(data, f, indent=4)
            global txt
            txt.setText(f'ваші гроші : {data["money"]}')

    def buy15():
        global data
        if data['money'] >= 9999999999:
            data['money'] -= 9999999999
            data['buylist'][14] = 1
            sodbtnlist[14].show()
            with open('data.json', 'w', ) as f:
                json.dump(data, f, indent=4)
            global txt
            txt.setText(f'ваші гроші : {data["money"]}')

    def col1():
        global data
        if data['buylist'][0] == 1:
            data['thiscar'] = 'img1.jpg'
            pixmap = QPixmap(data['thiscar']).scaled(128 , 128)
            global txtcar
            txtcar.setPixmap(pixmap)
            with open('data.json', 'w', ) as f:
                json.dump(data, f, indent=4)

    def col2():
        global data
        if data['buylist'][1] == 1:
            data['thiscar'] = 'img2.jpg'
            pixmap = QPixmap(data['thiscar']).scaled(128 , 128)
            global txtcar
            txtcar.setPixmap(pixmap)
            with open('data.json', 'w', ) as f:
                json.dump(data, f, indent=4)

    def col3():
        global data
        if data['buylist'][2] == 1:
            data['thiscar'] = 'img3.jpg'
            pixmap = QPixmap(data['thiscar']).scaled(128 , 128)
            global txtcar
            txtcar.setPixmap(pixmap)
            with open('data.json', 'w', ) as f:
                json.dump(data, f, indent=4)

    def col4():
        global data
        if data['buylist'][3] == 1:
            data['thiscar'] = 'img4.jpg'
            pixmap = QPixmap(data['thiscar']).scaled(128 , 128)
            global txtcar
            txtcar.setPixmap(pixmap)
            with open('data.json', 'w', ) as f:
                json.dump(data, f, indent=4)

    def col5():
        global data
        if data['buylist'][4] == 1:
            data['thiscar'] = 'img5.jpg'
            pixmap = QPixmap(data['thiscar']).scaled(128 , 128)
            global txtcar
            txtcar.setPixmap(pixmap)
            with open('data.json', 'w', ) as f:
                json.dump(data, f, indent=4)

    def col6():
        global data
        if data['buylist'][5] == 1:
            data['thishouse'] = 'img6.jpg'
            pixmap = QPixmap(data['thishouse']).scaled(128 , 128)
            global txthouse
            txthouse.setPixmap(pixmap)
            with open('data.json', 'w', ) as f:
                json.dump(data, f, indent=4)

    def col7():
        global data
        if data['buylist'][6] == 1:
            data['thishouse'] = 'img7.jpg'
            pixmap = QPixmap(data['thishouse']).scaled(128 , 128)
            global txthouse
            txthouse.setPixmap(pixmap)
            with open('data.json', 'w', ) as f:
                json.dump(data, f, indent=4)

    def col8():
        global data
        if data['buylist'][7] == 1:
            data['thishouse'] = 'img8.jpg'
            pixmap = QPixmap(data['thishouse']).scaled(128 , 128)
            global txthouse
            txthouse.setPixmap(pixmap)
            with open('data.json', 'w', ) as f:
                json.dump(data, f, indent=4)

    def col9():
        global data
        if data['buylist'][8] == 1:
            data['thishouse'] = 'img9.jpg'
            pixmap = QPixmap(data['thishouse']).scaled(128 , 128)
            global txthouse
            txthouse.setPixmap(pixmap)
            with open('data.json', 'w', ) as f:
                json.dump(data, f, indent=4)

    def col10():
        global data
        if data['buylist'][9] == 1:
            data['thishouse'] = 'img10.jpg'
            pixmap = QPixmap(data['thishouse']).scaled(128 , 128)
            global txthouse
            txthouse.setPixmap(pixmap)
            with open('data.json', 'w', ) as f:
                json.dump(data, f, indent=4)

    def col11():
        global data
        if data['buylist'][10] == 1:
            data['thismember'] = 'img11.jpg'
            pixmap = QPixmap(data['thismember']).scaled(128 , 128)
            global txtmamber
            txtmamber.setPixmap(pixmap)
            with open('data.json', 'w', ) as f:
                json.dump(data, f, indent=4)

    def col12():
        global data
        if data['buylist'][11] == 1:
            data['thismember'] = 'img12.jpg'
            pixmap = QPixmap(data['thismember']).scaled(128 , 128)
            global txtmamber
            txtmamber.setPixmap(pixmap)
            with open('data.json', 'w', ) as f:
                json.dump(data, f, indent=4)

    def col13():
        global data
        if data['buylist'][12] == 1:
            data['thismember'] = 'img13.jpg'
            pixmap = QPixmap(data['thismember']).scaled(128 , 128)
            global txtmamber
            txtmamber.setPixmap(pixmap)
            with open('data.json', 'w', ) as f:
                json.dump(data, f, indent=4)

    def col14():
        global data
        if data['buylist'][13] == 1:
            data['thismember'] = 'img114.jpg'
            pixmap = QPixmap(data['thismember']).scaled(128 , 128)
            global txtmamber
            txtmamber.setPixmap(pixmap)
            with open('data.json', 'w', ) as f:
                json.dump(data, f, indent=4)

    def col15():
        global data
        if data['buylist'][14] == 1:
            data['thismember'] = 'img15.jpg'
            pixmap = QPixmap(data['thismember']).scaled(128 , 128)
            global txtmamber
            txtmamber.setPixmap(pixmap)
            with open('data.json', 'w', ) as f:
                json.dump(data, f, indent=4)


    def buybitcoin():
        teh = requests.get('https://cex.io/api/last_price/BTC/USD')
        if teh.status_code == 200:
            cost = json.loads(teh.text)
            cost2 = float(cost["lprice"])
        else:
            print("sssddsdsddasfsgg")
        nonlocal polebuybitcoin
        count = int(polebuybitcoin.text())
        global data
        if data['money'] >= cost2*count:
            data['money'] -= cost2*count
            data['bitcoincount'] += count
            with open('data.json', 'w', ) as f:
                json.dump(data, f, indent=4)
            txt.setText(f'ваші гроші : {data["money"]}')
            nonlocal sbitcointxt
            sbitcointxt.setText(f'біткойнів у вас : {data["bitcoincount"]}')

    def sellbitcoin():
        teh = requests.get('https://cex.io/api/last_price/BTC/USD')
        if teh.status_code == 200:
            cost = json.loads(teh.text)
            cost2 = float(cost["lprice"])
        else:
            print("sssddsdsddasfsgg")
        nonlocal polesellbitcoin
        count = int(polesellbitcoin.text())
        global data
        if data['bitcoincount'] >= count :
            data['money'] += cost2 * count
            data['bitcoincount'] -= count
        with open('data.json', 'w', ) as f:
            json.dump(data, f, indent=4)
        txt.setText(f'ваші гроші : {data["money"]}')
        nonlocal sbitcointxt
        sbitcointxt.setText(f'біткойнів у вас : {data["bitcoincount"]}')


    bubutlist[0].clicked.connect(buy1)
    bubutlist[1].clicked.connect(buy2)
    bubutlist[2].clicked.connect(buy3)
    bubutlist[3].clicked.connect(buy4)
    bubutlist[4].clicked.connect(buy5)
    bubutlist[5].clicked.connect(buy6)
    bubutlist[6].clicked.connect(buy7)
    bubutlist[7].clicked.connect(buy8)
    bubutlist[8].clicked.connect(buy9)
    bubutlist[9].clicked.connect(buy10)
    bubutlist[10].clicked.connect(buy11)
    bubutlist[11].clicked.connect(buy12)
    bubutlist[12].clicked.connect(buy13)
    bubutlist[13].clicked.connect(buy14)
    bubutlist[14].clicked.connect(buy15)
    sbuybitcoinbtn.clicked.connect(buybitcoin)
    sodbtnlist[0].clicked.connect(col1)
    sodbtnlist[1].clicked.connect(col2)
    sodbtnlist[2].clicked.connect(col3)
    sodbtnlist[3].clicked.connect(col4)
    sodbtnlist[4].clicked.connect(col5)
    sodbtnlist[5].clicked.connect(col6)
    sodbtnlist[6].clicked.connect(col7)
    sodbtnlist[7].clicked.connect(col8)
    sodbtnlist[8].clicked.connect(col9)
    sodbtnlist[9].clicked.connect(col10)
    sodbtnlist[10].clicked.connect(col11)
    sodbtnlist[11].clicked.connect(col12)
    sodbtnlist[12].clicked.connect(col13)
    sodbtnlist[13].clicked.connect(col14)
    sodbtnlist[14].clicked.connect(col15)
    ssellbitcoinbtn.clicked.connect(sellbitcoin)

    window3.setLayout(mainline3)
    window3.show()
    window3.exec()


txt.setText(f'ваші гроші : {data["money"]}')

line1 = QHBoxLayout()
line2 = QHBoxLayout()

line1.addWidget(txtcar)
line1.addWidget(txthouse)
line1.addWidget(txtmamber)

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