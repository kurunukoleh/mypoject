from main import data
import json
def openbusnes(key , prise):
    if data["money"] >= prise:
        data["money"] -= prise
        data[key] += 1
        with open('data.json', 'w', ) as f:
            json.dump(data, f, indent=4)

def openbusnes1():
    openbusnes("busnes_count1" , 1)