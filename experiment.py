from PyQt5.QtWidgets import *
import json

with open('buttons.json', 'r', encoding='utf-8') as f:
    butons = json.load(f)

txt = butons['txt']
labels = []

app = QApplication([])
window = QWidget()
window.resize(800, 700)
mainline = QVBoxLayout()

for i in txt:
    labels.append(QLabel(i))

for i2 in labels:
    mainline.addWidget(i2)

window.setLayout(mainline)
window.show()
app.exec()