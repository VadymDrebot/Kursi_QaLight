def compare(x,y,z):
    while x<=y:
        print("ЗНАЧЕНИЕ A=",x)
        input("ПОКА ЧТО НЕТ, (press any key to continue)")
        x += z
    return x
a=int(input("input A: "))
b=int(input("input B: "))
c=int(input("input C: "))
print("\nДОЖДАЛИСЬ!!! ФИНАЛЬНЫЙ A: ",compare(a,b,c))