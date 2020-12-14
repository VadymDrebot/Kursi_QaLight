def compare(x,y):
     rezult=0
     for i in range(len(x)):
        if x[i]<y[i]:
           rezult=x
           break
        elif x[i]>y[i]:
           rezult=y
           break
     return rezult

string1=str(input("input first: "))
string2=str(input("input second: "))
a=compare(string1,string2)
if a==0:
    print("strings are eqial")
else:
    print("String" ,a," is bigger ")




