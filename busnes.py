from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import json

def open_window_busnes():
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
    window1 = QWidget()
    window1.resize(800, 700)
    mainline = QVBoxLayout()

    a = QLabel('g')
    mainline.addWidget(a)

    window1.setLayout(mainline)
    window1.show()
    app.exec()
