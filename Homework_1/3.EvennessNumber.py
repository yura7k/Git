# Знаходження парних та непарних чисел у заданому проміжку
# n - початок проміжку
# m - кінець проміжку

# Функція. Перевірка чи введені дані Input є числом
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

n = IsInt("Введіть початок проміжку: ")
m = IsInt("Введіть кінець проміжку: ")

listPar = []
listNep = []

if n >= m:
if n < m:
    for i in range(n, m + 1):
        if (i % 2) == 0:
            listPar.append(i)
        else:
            listNep.append(i)
    print("Непарні числа: ", listNep)
    print("Парні числа: ", listPar)
else:
    print("Введено некоректні дані!!!")