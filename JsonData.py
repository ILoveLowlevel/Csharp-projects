import json
import codecs

with open("Data.json",encoding='utf-8-sig') as file:
    Data = json.load(file)

#print(Data['Sprites'][0]['Coordinat_X1'])

print(Data['Coord'][0]['Coordinat3'])

newcoordinat = str(Data['Coord'][0]['Coordinat3'])
newsplittedcoordinat = newcoordinat.split(",")
FirstCoordinat = int(newsplittedcoordinat[0])
