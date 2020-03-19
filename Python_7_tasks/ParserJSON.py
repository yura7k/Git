import json

#  path to JSON file
fileDir = "D:/Python/Git/python_course/Python_7_tasks/"

""" Opens the file, if successful - reads it and returns the string
    
    Input:
        fileName - name file
    """
def openFile(fileName):
    try:
        fileExemple = open(fileDir + fileName)
        return fileExemple.read()
    except EOFError:
        print("Open open file")
    finally:
        fileExemple.close()


""" Function prints the data as a table
    Input:
        listData (list) - list of data
    """
def printTable(listData):
    if len(listData) < 1:
        print("No data to print!")
    else:
        lineTop = "+"
        lineTitle = "|"
        lineData = "|"
        
        listItem = listData[0]
        if isinstance(listItem, dict):
            for item in listItem.keys():
                lineTop = lineTop + ("".center(25, '-') + "+")
                lineTitle = lineTitle + item.center(25) + "|"
            print(lineTop)
            print(lineTitle)
            print(lineTop)
            for data in listData:
                for item in data:
                    if type(data[item]) == int:
                        data[item] = str(data[item])
                    lineData = lineData + data[item].center(25) + "|"
                print(lineData)
                lineData = "|"
        else:
            #lineTop = "+"
            lineTop = lineTop + ("".center(30, '-') + "+")
            print(lineTop)
            for item in listData:
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
def listBrands(file = 'Car_Model_List.json', sort = "none"):
    listJSON = json.loads(openFile(file))
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
def listModelByBrand(file = 'Car_Model_List.json', brand = "Tesla"):
    listJSON = json.loads(openFile(file))
    listOut = []
    dictModel = {}

    for item in listJSON:
        if item['Make'].lower() == brand.lower():
            dictModel['Make'] = item['Make']
            dictModel['Model'] = item['Model']
            dictModel['Year'] = str(item['Year'])
            listOut.append(dictModel)
            dictModel = {}
    if len(listOut) < 1:
        listOut.append("ERROR: wrong brand - " + brand)

    return listOut

fileJSON = 'Car_Model_List.json'

# Level 2 - Task1
printTable(listData= listBrands(sort='ask'))

# Level 2 - Task2
brand = input("Input name of brand auto: ")
printTable(listData= listModelByBrand(file= fileJSON, brand= brand))



# Test Data
# listBrands(sort = 'desk')
# data = [{"Make": "Audi", "Model": "Q3", "Category": "SUV"},{"Make": "Chevrolet", "Model": "Malibu", "Category": "Sedan"}]

