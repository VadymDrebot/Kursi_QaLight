#функция ввода трех значений
def input_info():
    a=input("input name: ")
    b=input("input age: ")
    c=input("input sex: ")
    return a,b,c

int_name,int_age,int_sex=input_info()
print(int_name)

