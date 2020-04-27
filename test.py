import datetime

date = input("Enter date:")

splitData = date.split(".")

print(datetime.date(int(splitData[2]), int(splitData[1]), int(splitData[0])))