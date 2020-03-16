import string

#  завантажуємо тукст з підготовленого файлу
try:
    fileExemple = open("D:/Python/Git/python_course/text.txt")
    strExemple = fileExemple.read()
    #  print(strExemple)
except EOFError:
    print("Open open file")
finally:
    fileExemple.close()

listAllWords = list(strExemple.split(' ')) #  ділимо текст на слова

#  Визначити, який відсоток слів у тексті починається з вказаної літери
#  за замовчуванням літера "s"
def charPercent(charExemple = "s"):
    count = 0
    for world in listAllWords:
        if world[0] == charExemple:
            count = count + 1
    percent = count * 100 / len(listAllWords)
    print(f"У тексті - {len(listAllWords)} слів.")
    print(f"У тексті - {count} слів, що починаються на '{charExemple}'.")
    print(f"Відсоток слів складає - {percent:.2f} %")
    
#  Знайти довжину самого короткого слова
def minLenWorld():
    minLen = 1
    for world in listAllWords:
        if len(world) <= minLen:
            minLen = len(world)
            minWorld = world

    print(f"Найменше слово в тексті - '{minWorld}' ")
    print(f"Його довжина - {minLen}")

#  Визначити на яку букву починається більшість слів у заданому тексті
def bestChar():
    #  рахуємо кількість слів з кожної букви алфавіта і пишемо в список
    abc = list(string.ascii_lowercase)
    listNumWorld = []
    for char in abc:
        count = 0
        for world in listAllWords:
            if world[0] == char:
                count = count + 1
        listNumWorld.append([char, count])

    #  визначаємо слів на яку літеру найбільше
    maxWorld = []
    maxSum = 0
    for item in listNumWorld:
        if int(item[1]) > maxSum:
            maxWorld = item
            maxSum = int(item[1])
    print(f"У тексті найбільше слів на літеру - '{maxWorld[0]}', їх кількість - {maxWorld[1]}")

#  У заданому тексті знищити всі слова з парними порядковими номерами.
#  пробував видаляти через pop(item) - не виходить]
def delEvenWorlds():
    tmpList = []
    for item in range(0, len(listAllWords), 2):
        tmpList.append(listAllWords[item])
    print("Скорочений списоr має ", len(tmpList), " слів")

#  У заданому тексті поміняти місцями перше й останнє слова.
def swapFirstLast():
    firstWordl = listAllWords[0]
    lastWorld = listAllWords[len(listAllWords)-1]
    listAllWords[0] = lastWorld
    listAllWords[len(listAllWords)-1] = firstWordl
    print(f"Тепер перший елемент {listAllWords[0]}, а останній {listAllWords[len(listAllWords)-1]}" )

charPercent('e')
minLenWorld()
bestChar()
delEvenWorlds()
swapFirstLast()