# за коментарі окреме дякую
# єдине в ідеалі їх старатися писати на англ
# * ось приблизний приклад
""" Should call summ of deposit

    Args:
        SumDeposit (int): Summ of the deposit.
        Dividends (int): Persent rate.
        Duration (int): Duration of the deposit in years.
        Type (int): 1 - simple / 2 - сomplex

    Returns:
        float: calculated rate
    """

# Функція обчислення суми депозиту, де параметри:
# SumDeposit - сума депозиту
# Dividends - відсоткова ставка
# Duration - тривалість вкладу
# Type - тип нарахування відсотків
#   1 - простий
#   2 - складний
# Повертає суму відсотків по депозиту

# розрахунок можна вивести в окрему функцію
# це дозволить уникнути помилок при повторному використанні коду
def getInterest(sumDeposit, dividends):
    return sumDeposit * dividends / 100

def DepositCalc(SumDeposit, Dividends, Duration, Type):
    # перша буква у змінних завжди маленька Type -> type, SumDeposit -> sumDeposit
    # виключення це константи, тоді TYPE, SUM_DEPOSIT
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

# Перевірка чи введені дані Input є числом
# якщо ні то пропонує ввести дані ще раз
# Повертає значення типу int
def IsInt(TextInput):
    a = 1
    while a == 1:
        try:
            TextOut = int(input(TextInput))
            break
        except ValueError:
            print("УВАГА!!! Ведено не числове значення!")
    return TextOut

# Змінні бажано назвивати згідно контексту + 31 стрічка коммент
# % ставка та сума може бути float (з крапкою)
SumD = IsInt("Вкажіть суму депозиту: ")
DivD = IsInt("Вкажіть відсоткову ставку: ")
DurD = IsInt("Вкажіть термін депозиту (роки): ")

print("Вкажіть тип нарахування відсотків: ")
TypD = IsInt("1 - Простий, 2 - Складний ")

dep = DepositCalc(SumD, DivD, DurD, TypD)

if dep != None : print("Через " + str(DurD) + " років Ваш депозит зросте на " + str(dep) + " грн.")