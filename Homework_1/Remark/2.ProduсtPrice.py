# Друк прайсу на товари за вказаними параметрами:
# Price - ціна товару
# Step - крок

# Опис фунцій див BankDeposit #4
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

# Опис змінних див BankDeposit #31
Name = input("Вкажіть назву товару: ")
# ціна може бути з копійками (float)
Price = IsInt("Вкажіть ціну товару: ")
Step = IsInt("Вкажіть крок прайсу: ")

print("Прайс на товар " + Name.upper())
print("+------------+--------------+")
print("|   Вага (г) |  Ціна (грн.) |")
print("+------------+--------------+")
for i in range(Step, 1000 + 1, Step):
    PriceI = Price / 1000 * i
    #також можна використовувати "".format(i, priceI)
    print("|" + "   " + str(i) + "г     |    " +  str(PriceI) + "     |")
    print("+------------+--------------+")