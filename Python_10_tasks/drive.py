import parserJSON
from taxi import Taxi

taxi = Taxi()
parce = taxi.dataJSON

taxi.getListTaxi(parce, "")
parserJSON.printTable(taxi.listTaxi, 19)

taxi.setTaxi()
taxi.setDistance()

taxi.getListTaxi(parce, taxi.name)
print("*******  YOU TAXI IS  *******".center(100))
parserJSON.printTable(taxi.listTaxi, 25)

taxi.getPriceTrip(taxi.name, taxi.distance)
print("****  Total price - ", taxi.priceTrip, " ****")

taxi.driveTrip(taxi.distance)
# перевіряв чи відпрацьовує...
taxi.driveTrip(taxi.distance)