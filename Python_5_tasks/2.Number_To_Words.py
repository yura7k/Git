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

number = int(input("Введіть ціле число < 9999: "))

if number in dictDigits.keys():
    print(dictDigits[number])
elif number // 10 < 10:
    numberRest = number % 10
    number = number - numberRest
    print(dictDigits[number], dictDigits[numberRest].lower())
elif number // 100 < 10:
    numberRest = number % 10
    number = number - numberRest
    numberRest10 = number % 100
    number = number - numberRest10
    print(dictDigits[number], dictDigits[numberRest10].lower(), dictDigits[numberRest].lower())
elif number // 1000 < 10:
    numberRest = number % 10
    number = number - numberRest
    numberRest10 = number % 100
    number = number - numberRest10
    numberRest100 = number % 1000
    number = number - numberRest100
    print(dictDigits[number], dictDigits[numberRest100].lower(), dictDigits[numberRest10].lower(),
        dictDigits[numberRest].lower())
else:
    print("Sorry... You input a big number: ", number)

""" Пробував ще так - не працює

strNumber = ""

if number // 1000 < 10:
    countThousant = number // 1000 * 1000
    numberRest = number - countThousant
    strNumber = strNumber + dictDigits[countThousant] + " "

    if numberRest // 100 < 10:
        countHungred = numberRest // 100 * 100
        numberRest = numberRest - countHungred
        if countHungred > 0: strNumber = strNumber + dictDigits[countHungred] + " "

        if numberRest // 10 < 10:
            countTeens = numberRest // 10 * 10
            numberRest = numberRest - countTeens
            if countTeens > 20: 
                strNumber = strNumber + dictDigits[countTeens] + " " 
            elif numberRest in dictDigits.keys():
                strNumber = strNumber + dictDigits[numberRest]
else:
    print("Sorry... You input a big number: ", number)

print(strNumber)"""