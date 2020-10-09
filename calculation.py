a=b=""
while type(a)!=int:                                      #  повторяем
    try:                                                 #  цикл
        a = int(input("Please input first number : "))   #  если
    except :                                             #  вводится
        print("Wrong input format. Please try again")    #  не  числовое значение
while type(b) != int:
    try:
        b = int(input("Please input second number : "))
    except:
        print("Wrong input format. Please try again")
print("")
print("1)  a + b = ",a+b)
print("2)  a - b = ",a-b)
print("3)  a * b = ",a*b)
if b!=0:                            #проверка деления на ноль
    print("4)  a / b = ",a/b)
else:
    print("4)  You can't devide by zero")
