# retrieve data from file
def getFile(fileName):
    with open(fileName) as file:
        return file.read()

# receive list of parts of json string
def getObjects(jsonString):
    specSymbols = ('[', ']', '{', '}', ':', ',')

    parts = []
    value = ""
    for symbol in jsonString:
        tmpValue = value.strip()

        if len(tmpValue) < 1 and symbol in specSymbols:
            parts.append(symbol)
        else:
            value += symbol

        if len(tmpValue) >= 1:
            if symbol == "\"":
                parts.append(tmpValue[1:])
                value = ""
            elif symbol in (',', '}', ']') and "\"" not in value:
                parts.append(float(value[:-1]))
                parts.append(symbol)
                value = ""

    return parts

# return json object
def parseObject(data):
    jsonObject = {}
    data = data[1:]
    
    # if first symbol is } returns empty object
    if data[0] == '}':
        return jsonObject, data[1:]

    # parse json object key values one by one
    while True:
        key = data[0]

        if data[1] != ':':
            raise Exception('Expected colon after key')

        value, data = tryToParseObject(data[2:])
        jsonObject[key] = value

        if data[0] == '}':
            return jsonObject, data[1:]
        elif data[0] != ',':
            raise Exception('Expected comma after pair')

        data = data[1:]

# return json array
def parseArray(data):
    jsonArray = []

    data = data[1:]

    # if first symbol ] returns empty array
    if data[0] == ']':
        return jsonArray, data[1:]
    
    # parse json items one by one
    while True:
        json, data = tryToParseObject(data)
        jsonArray.append(json)

        if data[0] == ']':
            return jsonArray, data[1:]
        elif data[0] != ',':
            raise Exception('Expected comma after pair')

        data = data[1:]

# check that item is object, array or value
def tryToParseObject(data, root = False):
    if root and data[0] not in ('{', '['):
        raise Exception('Incorrect structure')

    if data[0] == "[":
        return parseArray(data)
    elif data[0] == "{":
        return parseObject(data)
    
    return data[0], data[1:]

# call recursive algoritm for parsing json
def parseJsonString(jsonString):
    data = getObjects(jsonString)
    processedObject, data = tryToParseObject(data, True)
    return processedObject

jsonString = getFile("D:/Python/Git/python_course/Python_7_tasks/Car_Model_List.json")
processedObject = parseJsonString(jsonString)
print(processedObject)
# data = getObjects(jsonString)

# jsonArray, data = parseArray(data)

# print('')
# print(jsonArray)