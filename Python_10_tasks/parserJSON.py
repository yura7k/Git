import json

""" Function prints the data as a table
    Input:
        dataToPrint (list) - list of data
    """
def printTable(dataToPrint, count = 25):
    if len(dataToPrint) < 1:
        print("No data to print!")
    else:
        lineTop = "+"
        lineTitle = "|"
        lineData = "|"
        
        listItem = dataToPrint[0]
        if isinstance(listItem, dict):
            for item in listItem.keys():
                lineTop = lineTop + ("".center(count, '-') + "+")
                lineTitle = lineTitle + item.center(count) + "|"
            print(lineTop)
            print(lineTitle)
            print(lineTop)
            for data in dataToPrint:
                for item in data:
                    itemPrint = data[item]
                    if type(data[item]) == int or type(data[item]) == float:
                        itemPrint = str(data[item])
                    elif data[item] == None:
                        itemPrint = " "
                    lineData = lineData + itemPrint.center(count) + "|"
                print(lineData)
                lineData = "|"
        else:
            lineTop = lineTop + ("".center(count, '-') + "+")
            print(lineTop)
            for item in dataToPrint:
                lineData = lineData + (item.center(count) + "|")
                print(lineData)
                lineData = "|"

        print(lineTop)