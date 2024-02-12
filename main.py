from busnes import open_window_busnes
from shop import open_window_shop
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import json

data = {}

app = QApplication([])
app.setStyleSheet("""
    QWidget {
        background-color:#000000 ;
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
        background-color: #000000 ;
        color : #ffffff;
        font-size: 15px;
        border-radius: 5px ;
        border-color: #ff0000;
        border-style: solid;
    }

    QLabel:hover{
        background-color: #000000 ;
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

with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

def exitgame():
    with open('data.json', 'w', ) as f:
        json.dump(data, f, indent=4)
    app.quit()

def cklick():
    data["money"] += 1
    txt.setText(f'ваші гроші : {data["money"]}')


clbtn = QPushButton("cklick")
exitbtn = QPushButton("вийти з гри")
btnshop = QPushButton('магазин')
btnbusnes = QPushButton('бізнеси')
btnback = QPushButton('міні гра')

txt = QLabel(f'ваші гроші : {data["money"]}')
txt2 = QLabel('НА ХРЕСТИК НЕ НАТИСКАТИ')
txtcar = QLabel('ваша машина :')
txthouse = QLabel('ваша хата :')

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