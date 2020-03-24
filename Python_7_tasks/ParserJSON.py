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

#  parce JSON file to Python list
parceJSON = openFile()

""" Function prints the data as a table
    Input:
        dataToPrint (list) - list of data
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
                lineTop = lineTop + ("".center(30, '-') + "+")
                lineTitle = lineTitle + item.center(30) + "|"
            print(lineTop)
            print(lineTitle)
            print(lineTop)
            for data in dataToPrint:
                for item in data:
                    if type(data[item]) == int:
                        data[item] = str(data[item])
                    lineData = lineData + data[item].center(30) + "|"
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
        data (list) - list of data
        sort (str) - sort list by:
            none - no sorting
            ask - sort up
            desk - sort desk   

    Output:
        listBrand (list) - list All brands
    """
def listBrands(data= parceJSON, sort = "none"):
    listJSON = data
    listBrand = []

    if len(listJSON) < 1:
        listBrand.append("ERROR: No input data!")
        return listBrand
    else:
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

""" Level 2 - Task 2 - Return the list of models by input brands

    Input:
        data (list) - list of data
        brand (str) - name brand

    Output:
        listOut (list) - list All models by input brands
    """
def listModelByBrand(data= parceJSON, brand = "Tesla"):
    listJSON = data
    listOut = []

    if len(listJSON) < 1:
        listOut.append("ERROR: No input data!")
        return listOut
    else:    
        for item in listJSON:
            dictModel = {}
            if brand.lower() in item['Make'].lower():
                dictModel['Make'] = item['Make']
                dictModel['Model'] = item['Model']
                dictModel['Year'] = str(item['Year'])
                listOut.append(dictModel)
        if len(listOut) < 1:
            listOut.append("ERROR: wrong brand - " + brand)

        return listOut

""" Level 2 - Task 3 - Return the list of models by input model name

    Input:
        data (list) - list of data
        model (str) - seach model

    Output:
        listOut (list) - list All models by seach model
    """
def listModelByModel(data= parceJSON, model= "Model X"):
    listJSON = data
    listOut = []

    if len(listJSON) < 1:
        listOut.append("ERROR: No input data!")
        return listOut
    else:    
        for item in listJSON:
            dictModel = {}
            if model.lower() in item['Model'].lower():
                dictModel['Make'] = item['Make']
                dictModel['Model'] = item['Model']
                dictModel['Year'] = str(item['Year'])
                listOut.append(dictModel)
        if len(listOut) < 1:
            listOut.append("ERROR: wrong model - " + model)

    return listOut

""" Level 2 - Task 4 - Return the list of models by input year
    Input:
        data (list) - list of data
        Year (str) - seach Year

    Output:
        listOut (list) - list All models by seach year
    """
def listModelByYear(data= parceJSON, year= "2019"):
    listJSON = data
    listOut = []
    listYear = []

    if ',' in year:
        listYear = year.split(',')
    elif '-' in year:
        year = year.split('-')
        for i in range(int(year[0]), int(year[1]) + 1):
            #  через те що на 187 стрічці, я конвертую в str
            #  довелось конвертувати і тут щоб не було конфлікту
            listYear.append(str(i))
    else:
        listYear.append(year)

    if len(listJSON) < 1:
        listOut.append("ERROR: No input data!")
        return listOut
    else:    
        for itemYear in listYear:
            for item in listJSON:
                dictModel = {}
                if itemYear.lower() in item['Year'].lower():
                    dictModel['Make'] = item['Make']
                    dictModel['Model'] = item['Model']
                    dictModel['Year'] = str(item['Year'])
                    listOut.append(dictModel)
        if len(listOut) < 1:
            listOut.append("ERROR: no model for - " + year)

    return listOut

""" Level 3 - Task 2 - Print the list of models by page
    Input:
        data (list) - list of data
        step (int) - count strings on print page
        start (int) - first item for print
    """
def printByStep(data= parceJSON, step= 5, start = 0):
    while True:
        #  перевіряємо чи список більший за кількість елементів на сторінці
        if len(data) > start + step:    
            #  якщо так друкуємо першу сторінку і виводимо повідомлення
            printTable(dataToPrint= data[start:start + step])
            key = input("Press any <ENTER> to next or ANY SYMBOL to previos: ")
            #  якщо немає символів друкуємо наступну сторінку
            if key == '' and start >= 0:
                firstEl = start + step
                printByStep(data= data, step= step, start= firstEl)
                break
            #  інакше перевіряємо чи можливо надрукувати попередню сторінку
            elif key != '' and start >= step:
                firstEl = start - step
                printByStep(data= data, step= step, start= firstEl)
                break
            #  якщо попередньої немає друкуємо помилку
            else:
                error = ["No previos page"]
                printTable(dataToPrint= error)
                break
        else:
            printTable(dataToPrint= data[start:])
            break

# Level 2 - Task 1
#dataBrands = listBrands(sort='ask')
#printTable(dataToPrint= dataBrands)

# Level 2 - Task 2
brand = input("Input name of brand auto: ")
dataModels = listModelByBrand(brand= brand)
printTable(dataToPrint= dataModels)

# Level 2 - Task 3 
model = input("Input model auto: ")
dataModels = listModelByModel(data= dataModels, model= model)
# printTable(dataToPrint= dataModels)

# Level 3 - Task 2 by step 
printByStep(data= dataModels) 

# Level 2 - Task 4
# Працює все послідовно, тобто відбирає  спочатку бренд
# Потім модель
# Потім по року
inYear = input("Input Yaer of model auto (sep by ',' or '-'): ")
dataModels = listModelByYear(data= dataModels, year= inYear)
printTable(dataToPrint= dataModels)