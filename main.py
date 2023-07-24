import pandas as pd
import numpy as np

data = pd.read_excel('TEST.xlsx')
data = data.replace('SOFA', 'SOFIA')
data = data.replace('Betsiboka', 'BETSIBOKA')
data = data.replace('PORT_BERGE', 'PORT_BERGER')
data = data.replace('AMBATO_BOENY', 'AMBATOBOENY')
data = data.replace('Maevatanana', 'MAEVATANANA')
data = data[data.REGION != ' ']

def listerElement(element):
    for index, value in enumerate(element):
        print(index+1, ':', value)

print("Liste des regions")
dataRegions = data.REGION.unique()
listerElement(dataRegions)
print()
choixRegion = input("Choisir un region : ")
region = dataRegions[(int(choixRegion))-1]

print("Liste des districts dans la region ", region, " : ")
dataDistrics = data.District[data.REGION == region].unique()
listerElement(dataDistrics)
print()
choixDistrict = input("Choisr un District : ")
district = dataDistrics[(int(choixDistrict))-1]

print("Liste des communes dans la district ", district, " : ")
dataCommune = data.Commune[data.District == district].unique()
listerElement(dataCommune)
print()
choixCommune = input("Choisir un Commune : ")
commune = dataCommune[int(choixCommune)-1]

print("Liste des fokontany dans la commune ", commune, " : ")
dataFokontany = data.Fokontany[data.Commune == commune].unique()
listerElement(dataFokontany)
print()
choixFokontany = input("choisir un Fokontany : ")
fokontany = dataFokontany[(int(choixFokontany))-1]

print(region, ">", district, ">", commune, ">", fokontany)
print()