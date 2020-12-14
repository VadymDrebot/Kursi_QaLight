spisok=[]                                   #
import random                               #
for i in range(5):                          #
    spisok.append(random.randint(0,9))      # создание списка цифр
print("Your random list is: ",spisok)
input_digit = int(input("Please input digit : "))
kolvo_povtoreniy=0
indexes=[]                                  # список для номеров позиций повторений
count=1
for item in spisok:
    if item==input_digit:
        indexes.append(count)
        kolvo_povtoreniy+=1
    count+=1
if kolvo_povtoreniy==0:
    print("There is no digit ",input_digit," in the list")
else:
    print("\nDesired digit: ", input_digit , "\nWas found: ", kolvo_povtoreniy, "times \nIn index(es): ", indexes)

