import random
def create_list(): # создание списка из 10-ти чисел
    spisok=[]
    for i in range(10):
        spisok.append(random.randint(0,10))
    return spisok
###################################
def povtori(spis):      # удаляет из списка одинаковые элементы
    lenth = len(spis)
    i = 0
    while i < lenth:
        y = i + 1
        while y < lenth:
            if spis[y] == spis[i]:
         #       print("deleting", spis[y])
                spis.pop(y)
                lenth -= 1
                y = i + 1
            else:
                y += 1
        i += 1
    return spis
########################################

spisok1=create_list()
spisok2=create_list()
spisok_rezult=[]
print("Первый список: ",spisok1)
print("Второй список: ",spisok2)
for i in spisok1:
    if i in spisok2:
        spisok_rezult.append(i)
        spisok2.remove(i)
print("Список после сравнения: ",spisok_rezult)
print("Список без повторных элементов: ",povtori(spisok_rezult))


