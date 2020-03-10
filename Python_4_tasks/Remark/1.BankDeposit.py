""" Дякую за допомогу з коментарем, сам поки так не напишу :)
    
    Should call summ of deposit

    Args:
        SumDeposit (int): Summ of the deposit.
        Dividends (int): Persent rate.
        Duration (int): Duration of the deposit in years.
        Type (int): 1 - simple / 2 - сomplex

    Returns:
        float: calculated rate
    """

""" Check whether the input data is a number

    Returns:


    """
def isInt(textInput):
    a = 1
    while a == 1:
        try:
            numberOut = int(input(textInput))
            break
        except ValueError:
            print("УВАГА!!! Ведено не числове значення!")
    return TextOut

def getDepositCalc(sumDeposit, dividends, duration, type):
    if Type == 1:
        # SumDividends = getInterest(SumDeposit, Dividends) * Duration
        SumDividends = SumDeposit * Dividends / 100 * Duration
        return float("{:.2f}".format(SumDividends))
    elif Type == 2:
        SumTemp = SumDeposit
        for i in range(Duration):
            SumDividends = SumDeposit * Dividends / 100
            #SumDeposit = SumDeposit + getInterest(SumDeposit, Dividends)
            SumDeposit =  SumDeposit + SumDividends
        SumDividends = SumDeposit - SumTemp
        return float("{:.2f}".format(SumDividends))
    else:
        print("Невірно вказано тип нарахування відсотків!")
        pass
    # повернення результату можна винести за межі if, це дозволить зменшити дублювання коду
    #return float("{:.2f}".format(SumDividends))

# Змінні бажано назвивати згідно контексту + 31 стрічка коммент
# % ставка та сума може бути float (з крапкою)
SumD = IsInt("Вкажіть суму депозиту: ")
DivD = IsInt("Вкажіть відсоткову ставку: ")
DurD = IsInt("Вкажіть термін депозиту (роки): ")

print("Вкажіть тип нарахування відсотків: ")
TypD = IsInt("1 - Простий, 2 - Складний ")

dep = DepositCalc(SumD, DivD, DurD, TypD)

if dep != None : print("Через " + str(DurD) + " років Ваш депозит зросте на " + str(dep) + " грн.")