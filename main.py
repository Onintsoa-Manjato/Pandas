import pandas as pd
data = pd.read_excel('TEST.xlsx')
def listerElement(element):
    for index, value in enumerate(element):
        print(index, ':', value)

while True:
    dataRegions = data.REGION.unique()
    print("Liste des regions")
    listerElement(dataRegions)
    choixRegion = input("Choisir un region : ")
    region = dataRegions[int(choixRegion)]
    dataDistrics = data.District[data.REGION == region].unique()
    print("Liste des districts dans la region ", region, " : ")
    listerElement(dataDistrics)
    choixDistrict = input("Choisr un District : ")
    district = dataDistrics[int(choixDistrict)]
    dataCommune = data.Commune[data.District == district].unique()
    print("Liste des communes dans la district ", district, " : ")
    listerElement(dataCommune)
    choixCommune = input("Choisir un Commune : ")
    commune = dataCommune[int(choixCommune)]
    dataFokontany = data.Fokontany[data.Commune == commune].unique()
    print("Liste des fokontany dans la commune ", commune, " : ")
    listerElement(dataFokontany)
    choixFokontany = input("choisir un Fokontany : ")
    fokontany = dataFokontany[int(choixFokontany)]
    print(region, ">", district, ">", commune, ">", fokontany)
    break   