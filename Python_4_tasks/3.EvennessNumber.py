""" Find the even and odd numbers in the given interval

    Args:
        n (int) - begining interval
        m (int) - end interval

    Returns:
        Print two list even and odd numbers
    """
def evenOddNumber(n, m):
    listParni = []
    listNeparni = []
    if n >= m:
        print("Введено некоректні дані!!!")
        return

    for i in range(n, m + 1):
        if (i % 2) == 0:
            listParni.append(i)
        else:
            listNeparni.append(i)

    print("Непарні числа: ", listNeparni)
    print("Парні числа: ", listParni)  
    
    return

    
"""Check whether the input data is a int

    Returns:
        int number or error"""

def isInt(textInput):
    a = 1
    while a == 1:
        try:
            textOut = int(input(textInput))
            break
        except ValueError:
            print("УВАГА!!! Ведено не числове значення!")
    return textOut

intBegin = isInt("Введіть початок проміжку: ")
intEnd = isInt("Введіть кінець проміжку: ")

evenOddNumber(intBegin, intEnd)  

""" Переробив завдання через функцію
    Змінив опис
    забрав лишне вкладення"""