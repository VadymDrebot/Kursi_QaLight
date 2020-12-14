def convert_seconds(time):
    from datetime import timedelta
    time=timedelta(seconds=x)
    return time

try:
    x=int(input("Введите кол-во секунд: "))
    print(convert_seconds(x))
except:
    time=print("Секунды нужно вводить в числом")





