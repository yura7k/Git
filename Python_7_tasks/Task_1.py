fileDir = "D:/Python/Git/python_course/Python_7_tasks/"

""" Opens the file, if successful - reads it and returns the string
    
    Input:
        fileName - name file
    """
def openFile(fileName):
    #  завантажуємо текст з підготовленого файлу
    try:
        fileExemple = open(fileDir + fileName)
        return fileExemple.read()
    except EOFError:
        print("Open open file")
    finally:
        fileExemple.close()

""" Функція парсить JSON файл та повертає свисок, кожен елемент якого є словником (dict)

    Input:
        file - шлях до файлу

    Output:
        listCar (list) - де елементи списку словник (dict) одного елементу JSON
    """
def parceJson():
    strExemple = openFile("Car_Model_List.json")
    # strExemple = strExemple.strip('[]')
    listTmp = strExemple.splitlines()
    listCar = []
    tempDict = {}
    for item in listTmp:
        item = item.strip()
        if item == '{' or item == '' or item == '[':
            continue
        elif item != '},':
            item = item.partition(':')
            keyDict = item[0].strip(' ",')
            itemDict = item[2].strip(' ",')
            tempDict[keyDict] = itemDict
        else:
            listCar.append(tempDict)
            tempDict = {}
    return listCar

""" printCar - друкує список авто за вказаним роком
    """
def printCar(Year = '2020'):
    #  друкуємо заголовок таблички
    lineTop = ("+" + "".center(10, '-') + "+" + "-".center(20, "-") + "+" + 
            "-".center(35, "-") + "+" + "-".center(40, "-") +"+")
    print(lineTop)
    print("|" + "Year".center(10) + "|" + "Make".center(20) + "|" + 
            "Model".center(35) + "|" + "Category".center(40) +"|")
    print(lineTop)

    #  Парсим наш json
    tmrJson = parceJson()
    
    for item in tmrJson:
        if item.get('Year') != Year: # вивести список авто 2020 року
            print(lineTop)
            break
        lineCar = ("|" + item.get('Year').center(10) + "|" + item.get('Make').center(20) + "|" + 
            item.get('Model').center(35) + "|" + item.get('Category').center(40) +"|")
        print(lineCar)
        
printCar()