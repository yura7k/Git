import json
import random

class Taxi:
    def __init__(self):
        #  шлях до файлу prices.json
        self.name = ""
        self.distance = 0
        self.listTaxi = []
        
        file = "D:/Python/Git/python_course/Python_10_tasks/prices.json"
        try:
            fileData = open(file)
            self.dataJSON = json.loads(fileData.read())
        except EOFError:
            print("Error open file!!!")
        finally:
            fileData.close()

    def setTaxi(self):
        self.name = input("Input name Taxi from list above: ")

    def setDistance(self):
        while True:
            try:
                distance = float(input("Input Distance (km): "))
                self.distance = distance
                break
            except ValueError:
                print("ERROR!!! Input incorect number!")

    def getListTaxi(self, data, name):     
        self.listTaxi = []   
        
        if len(data) < 1:
            self.listTaxi.append("ERROR: No input data!")
        else:
            listJSON = data
            for el in listJSON:
                for item in listJSON[el]:
                    dictModel = {}
                    if self.name.lower() in item['display_name'].lower():
                        # for i in item:
                        #    dictModel[i] = item[i]
                        dictModel['display_name'] = item['display_name']
                        dictModel['high_estimate'] = item['high_estimate']
                        dictModel['low_estimate'] = item['low_estimate']
                        dictModel['estimate'] = item['estimate']
                        #dictModel['currency_code'] = item['currency_code']
                        self.listTaxi.append(dictModel)
            if len(self.listTaxi) < 1:
                self.listTaxi.append("ERROR: wrong name - " + self.name)

    def getPriceTrip(self, name, distance):
        if name and distance:
            highEst = 0
            lowEst = 0
            for item in self.listTaxi:
                if name.lower() in item['display_name'].lower():
                    highEst = int(item['high_estimate'])
                    lowEst = int(item['low_estimate'])
                    self.priceTrip = distance * random.randint(lowEst, highEst)
        else:
            print("No input name taxi or distance!!!")