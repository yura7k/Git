# Функція обчислення суми депозиту, де параметри:
# SumDeposit - сума депозиту
# Dividends - відсоткова ставка
# Duration - тривалість вкладу
# Type - тип нарахування відсотків
#   1 - простий
#   2 - складний
# Повертає суму відсотків по депозиту

def DepositCalc(SumDeposit, Dividends, Duration, Type):
    if Type == 1:
        SumDividends = SumDeposit * Dividends / 100 * Duration
        return float("{:.2f}".format(SumDividends))
    elif Type == 2:
        SumTemp = SumDeposit
        for i in range(Duration):
            SumDividends = SumDeposit * Dividends / 100
            SumDeposit =  SumDeposit + SumDividends
        SumDividends = SumDeposit - SumTemp
        return float("{:.2f}".format(SumDividends))
    else:
        print("Невірно вказано тип нарахування відсотків!")
        pass

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

SumD = IsInt("Вкажіть суму депозиту: ")
DivD = IsInt("Вкажіть відсоткову ставку: ")
DurD = IsInt("Вкажіть термін депозиту (роки): ")
print("Вкажіть тип нарахування відсотків: ")
TypD = IsInt("1 - Простий, 2 - Складний ")

dep = DepositCalc(SumD, DivD, DurD, TypD)

if dep != None : print("Через " + str(DurD) + " років Ваш депозит зросте на " + str(dep) + " грн.")