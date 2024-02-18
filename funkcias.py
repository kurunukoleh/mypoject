from setings import data
import json

def openbusnes1():
    if data["money"] >= 1000:
        data["money"] -= 1000
        data["busnes_count1"] += 1
        with open('data.json', 'w', ) as f:
            json.dump(data, f, indent=4)

def openbusnes2():
    if data["money"] >= 5000:
        data["money"] -= 5000
        data["busnes_count2"] += 1
        with open('data.json', 'w', ) as f:
            json.dump(data, f, indent=4)

def openbusnes3():
    if data["money"] >= 50000:
        data["money"] -= 50000
        data["busnes_count3"] += 1
        with open('data.json', 'w', ) as f:
            json.dump(data, f, indent=4)

def openbusnes4():
    if data["money"] >= 1000000:
        data["money"] -= 1000000
        data["busnes_count4"] += 1
        with open('data.json', 'w', ) as f:
            json.dump(data, f, indent=4)

def openbusnes5():
    if data["money"] >=2000000 :
        data["money"] -= 2000000
        data["busnes_count5"] += 1
        with open('data.json', 'w', ) as f:
            json.dump(data, f, indent=4)

def openbusnes6():
    if data["money"] >= 1000000000:
        data["money"] -= 1000000000
        data["busnes_count6"] += 1
        with open('data.json', 'w', ) as f:
            json.dump(data, f, indent=4)