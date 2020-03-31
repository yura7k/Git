import json
import random

class Taxi:
    def __init__(self):
        #  шлях до файлу prices.json
        self.name = ""
        self.distance = 0
        self.drove = 0
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
                if isinstance(item, dict):
                    if type(item['high_estimate']) == int or type(item['high_estimate']) == float:
                        highEst = item['high_estimate']
                    if type(item['low_estimate']) == int or type(item['low_estimate']) == float:
                        lowEst = item['low_estimate']
                    self.priceTrip = distance * random.randint(lowEst, highEst)
                else:
                    self.priceTrip = 0
            if highEst == 0 and lowEst == 0 and self.priceTrip != 0:
                self.priceTrip = "You Trip is FREE!!!"
        else:
            print("No input name taxi or distance!!!")
    
    def driveTrip(self, distance):
        input("\nPress <ENTER> to Start...")
        if distance > 0 and self.priceTrip != 0:
            while distance > 0:
                trip = random.randint(1, distance)
                distance -= trip
                self.distance = distance
                self.drove += trip
                print("You drove - ", trip, ", left - ", distance)
            
            print("\nTrip is Finish!")
            print("  Total drove - {} km".format(self.drove))
            print("  Total price - {:.2f} USD".format(self.priceTrip))
        elif self.priceTrip == 0:
            print("You enter wrong taxi", self.name)
        else:
            print("You already in state!")
    