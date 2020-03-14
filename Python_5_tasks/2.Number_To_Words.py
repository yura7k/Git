""" Program print entered number in words

    Input:
        number (int) : any number < 9999

    Print:
        Print number in words
    """

dictDigits = {0: 'Нуль', 1: 'Один', 2: 'Два', 3: 'Три', 4: 'Чотири', 5: 'П\'ять', 
                6: 'Шість', 7: 'Сім', 8: 'Вісім', 9: 'Дев\'ять', 10: 'Десять', 
                11: 'Одинадцять', 12: 'Дванадцять', 13: 'Тринадцять', 14: 'Чотирнадцять', 
                15: 'П\'ятнадцять', 16: 'Шістнадцять', 17:'Сімнадцять', 18:'Вісімнадцять', 
                19:'Дев\'ятнадцять', 20:'Двадцять', 30:'Тридцять', 40:'Сорок', 50:'П\'ятдесят', 
                60:'Шістдесят', 70:'Сімдесят', 80:'Вісімдесят', 90:'Дев\'яносто', 100:'Сто', 
                200:'Двісті', 300:'Триста', 400:'Чотириста', 500:'П\'ятсот', 600:'Шістсот', 
                700:'Сімсот', 800:'Вісімсот', 900:'Дев\'ятсот', 1000:'Одна тисяча', 
                2000:'Дві тисячі', 3000:'Три тисячі',  4000:'Чотири тисячі',  5000:'П\'ять тисяч',  
                6000:'Шість тисяч', 7000:'Сім тисяч', 8000:'Вісім тисяч', 9000:'Дев\'ять тисяч'}

""" digitNumber - Function searches for the digit number and returns the value to the list

    Args:
        inputNumber (int): Input number
    
    Returns:
        list : numberRest wthere:
            list[0]- number of thousant
            lisl[1]- number of hungred
            list[2]- number of tens
    # теоретично це можна розширити розширивци словник
    # на англійській було б ленше, там немає закінчень))
    """
def digitNumber(inputNumber):
    numDivision = 1000
    numberRest = []

    while  numDivision >= 10:
        resultDiv = inputNumber // numDivision
        numberRest.append(resultDiv)
        inputNumber = inputNumber - resultDiv * numDivision
        numDivision = int(numDivision / 10)
    
    return numberRest

number = int(input("Введіть ціле число < 9999: "))

listDigit = digitNumber(number)
lenList = len(listDigit)
strNumber = ""

if number > 9999:
    print("Sorry... You input a big number: ", number)      
elif lenList > 0:
    numDivision = 1000  # число на яке дылимо
    numTMP = 0  # чимсове число сума вже написаних чисел
    for i in range(lenList):
        intItem = int(listDigit[i])
        if intItem != 0 and intItem*numDivision >= 20:  # те шо неправильно писало
            strNumber = strNumber + dictDigits[numDivision * intItem] + " "
            numTMP = numTMP + numDivision * intItem
        numDivision = numDivision / 10
    number = number - numTMP
    if number in dictDigits.keys():
        strNumber = strNumber + dictDigits[number]
    print(strNumber.capitalize())  