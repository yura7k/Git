""" Дякую за допомогу з коментарем, сам поки так не напишу :)
    """
"""Should call summ of deposit

    Args:
        sumDeposit (float): Summ of the deposit.
        dividends (float): Persent rate.
        duration (int): Duration of the deposit in years.
        type (int): 1 - simple / 2 - сomplex

    Returns:
        float: calculated rate
    """

def getDepositCalc(sumDeposit, dividends, duration, type):
    if type == 1:
        sumDividends = sumDeposit * dividends / 100 * duration
        return float("{:.2f}".format(sumDividends))
    elif type == 2:
        sumTemp = sumDeposit
        for i in range(duration):
            sumDividends = sumDeposit * dividends / 100
            sumDeposit =  sumDeposit + sumDividends
        sumDividends = sumDeposit - sumTemp
        return float("{:.2f}".format(sumDividends))
    else:
        print("Невірно вказано тип нарахування відсотків!")
        pass

""" Check whether the input data is a number

    Returns:
        int or float digit
    """
def isNumber(textInput):
    a = 1
    while a == 1:
        try:
            numberOut = float(input(textInput))
            if numberOut.is_integer(): numberOut = int(numberOut)
            break
        except ValueError:
            print("УВАГА!!! Ведено не числове значення!")
    return numberOut

floatSumDeposit = isNumber("Вкажіть суму депозиту: ")
floatDividents = isNumber("Вкажіть відсоткову ставку: ")
intDuration = isNumber("Вкажіть термін депозиту (роки): ")

print("Вкажіть тип нарахування відсотків: ")
bolType = isNumber("1 - Простий, 2 - Складний ")

floatDeposit = getDepositCalc(floatSumDeposit, floatDividents, intDuration, bolType)

if floatDeposit != None : print("Через {0} років Ваш депозит зросте на {1} грн.".format(str(intDuration), str(floatDeposit)))

""" Все ніби працює, але якщо ввести термін депозиту float, то все зламається
    """