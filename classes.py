#класс СОБАКА с методами: init, sit,jump,info
class Dog():
    count=0                     #счетчик собак
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
        Dog.count+=1
        print("dog ",self.name," is created")

    def sit(self):
        print(self.name+" собака села")
    def jump(self):
        print(self.name + " прыгнул")
    def info(self):
        print("собака ",self.name, " is ",self.sex," and it is ",self.age," years old")

def input_info():          # функция ДЛЯ ВВОДА инфы о собаке
    a=input("input name: ")
    b=int(input("input age: "))
    c=input("input sex: ")
    return a,b,c

int_name,int_age,int_sex=input_info()      #присваиваем переменным параметры из вызванной функции
dog1 = Dog(int_name,int_age,int_sex)       #определяем первую собаку
if str(input("do you have another dog? ")) == "y":
    int_name, int_age, int_sex = input_info()
    dog2 = Dog(int_name, int_age, int_sex )

print()
dog_choise = int(input("which dog do you prefer?" + dog1.name + " or " + dog2.name))   # выбор собаки
if dog_choise == 1:
    actdog = dog1                           # actdog-- собака с которой будем работать
elif dog_choise == 2:
    actdog = dog2

command = int(input("\nChoose the command(1-sit or 2-jump: "))

if command == 1:
    print(actdog.sit())
elif command == 2:
    print(actdog.jump())

if str(input("all info? ")) == "y":
    print(actdog.info())
    print("you have",Dog.count,"dogs")


