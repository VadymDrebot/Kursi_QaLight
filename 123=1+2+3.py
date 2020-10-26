def summa(num):
    sum=0
    for i in range(len(num)):
        sum=sum+int(num[i])
    print(sum)
    return

try:
    a=input("input only numbers: ")
    b=int(a)
    summa(a)
except:
    print("wrong format")
