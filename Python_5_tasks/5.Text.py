strExemple = "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?"

#  Виводить кількість речень у тексті 
def countSentences():
    punctuation = ['.', '!', '?', '...', '!?', '!!!']
    count = 0
    for i in strExemple:
        if i in punctuation:
            count = count + 1
    return count

#  Підрахувує кількість слів «quis» (по замовчуванню) або іншого яке передається
def countWorld(world = 'quis'):
    count = strExemple.lower().count(world.lower()) #  понижуємо регіст щоб не залежало від регістру
    return count

#  Підрахувує кількість символів з пробілами count
#  Підрахувує кількість символів без пробілів countWithoutSpace
def countChar():
    count = strExemple.count('')
    countWithoutSpace = strExemple.replace(' ', '').count('')
    return count, countWithoutSpace

#  Виводить на екран перші 120 символів та додати «…» після останнього слова. 
#  Необхідно видалити останнє слово, якщо воно не буде виведено повністю.
def print120(count = 120):
    punctuation = ['.', '!', '?', '-', ',']
    string120 = strExemple[:count]
    #  шукаємо чи останій символ пробіл, якщо ні знаходимо останій пробіл
    if strExemple[count] == " ":
        string120 = strExemple[:count] + "..."
    else:
        findSpace = string120.rfind(" ")
        if string120[findSpace-1] in punctuation: # також перевіряємо чи кінецб не розділовий знак
            findSpace = findSpace - 1
        string120 = string120[:findSpace] + "..."
    print(string120)

print("Кількість речень у тексті - ", countSentences())
world = 'QUis' # input("Введіть пошукове слово: ").lower()
print(f"Кількість слів {world} - ", countWorld(world))
print("Кількість символів з пробілами - ", countChar()[0])
print("Кількість символів без пробілами - ", countChar()[1])
print120(120)