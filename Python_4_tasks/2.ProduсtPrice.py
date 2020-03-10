""" Print the price for goods to the following parameters:
    
    Args:
        Price (float) - price of the product
        Step (int) - price step
"""

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

stsName = input("Вкажіть назву товару: ")
floatPrice = isNumber("Вкажіть ціну товару: ")
intStep = isNumber("Вкажіть крок прайсу: ")

print("Прайс на товар " + stsName.upper())
print("+---------------+---------------+")
print("|   Вага (г)\t|  Ціна (грн.)\t|")
print("+---------------+---------------+")
for i in range(intStep, 1000 + 1, intStep):
    floatPriceI = floatPrice / 1000 * i
    print("|" + "   {0} г\t|    {1:.2f}\t|".format(i, floatPriceI))
    print("+---------------+---------------+")

""" Переробив фуркцію isInt на isNumber
    зробив вирівнювання через табуляцію 
    а сам вивід через  format """