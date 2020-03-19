import json

#  path to JSON file
fileDir = "D:/Python/Git/python_course/Python_7_tasks/"
#  name JSON file
fileName = "Car_Model_List.json"

""" Opens the file, if successful - reads it and convert 
    JSON object to Python object
    
    Input:
        fileName - name file

    Output:
        dataJSON(list) - Python list where elements is DICT
    """
def openFile(file= fileName):
    try:
        fileData = open(fileDir + file)
        dataJSON = json.loads(fileData.read())
        return dataJSON
    except EOFError:
        print("Open open file")
    finally:
        fileData.close()

""" Function prints the data as a table
    Input:
        listData (list) - list of data
    """
def printTable(dataToPrint):
    if len(dataToPrint) < 1:
        print("No data to print!")
    else:
        lineTop = "+"
        lineTitle = "|"
        lineData = "|"
        
        listItem = dataToPrint[0]
        if isinstance(listItem, dict):
            for item in listItem.keys():
                lineTop = lineTop + ("".center(25, '-') + "+")
                lineTitle = lineTitle + item.center(25) + "|"
            print(lineTop)
            print(lineTitle)
            print(lineTop)
            for data in dataToPrint:
                for item in data:
                    if type(data[item]) == int:
                        data[item] = str(data[item])
                    lineData = lineData + data[item].center(25) + "|"
                print(lineData)
                lineData = "|"
        else:
            lineTop = lineTop + ("".center(30, '-') + "+")
            print(lineTop)
            for item in dataToPrint:
                lineData = lineData + (item.center(30) + "|")
                print(lineData)
                lineData = "|"
            
        print(lineTop)

""" Level 2 - Task1 - Return the list of car brands

    Input:
        file (str) - file name
        sort (str) - sort list by:
            none - no sorting
            ask - sort up
            desk - sort desk   

    Output:
        listBrand (list) - list All brands
    """
def listBrands(sort = "none"):
    
    listJSON = openFile()
    listBrand = []

    for item in listJSON:
        if item['Make'] in listBrand:
            continue
        else:
            listBrand.append(item['Make'])

    if sort == 'ask':
        listBrand.sort()
    elif sort == 'desk':
        listBrand.sort(reverse=True)

    return listBrand

""" Level 2 - Task2 - Return the list of models by input brands

    Input:
        file (str) - file name
        brand (str) - name brand

    Output:
        listOut (list) - list All models by input brands
    """
def listModelByBrand(brand = "Tesla"):
    listJSON = openFile()
    listOut = []
    
    for item in listJSON:
        dictModel = {}
        if item['Make'].lower() == brand.lower():
            dictModel['Make'] = item['Make']
            dictModel['Model'] = item['Model']
            dictModel['Year'] = str(item['Year'])
            listOut.append(dictModel)
    if len(listOut) < 1:
        listOut.append("ERROR: wrong brand - " + brand)

    return listOut

# Level 2 - Task1
dataBrands = listBrands(sort='ask')
printTable(dataToPrint= dataBrands)

# Level 2 - Task2
brand = input("Input name of brand auto: ")
dataModels = listModelByBrand(brand= brand)
printTable(dataToPrint= dataModels)

# Test Data
# listBrands(sort = 'desk')
# data = [{"Make": "Audi", "Model": "Q3", "Category": "SUV"},{"Make": "Chevrolet", "Model": "Malibu", "Category": "Sedan"}]

