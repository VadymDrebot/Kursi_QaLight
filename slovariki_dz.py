
def first_dict():
    tel_em={'tel': input("input tel: "), 'email':input("input email: ")}
    print(tel_em)
    name1=input("name: ")
    info1=dict.fromkeys([name1],tel_em)
    return info1

def second_dict():
    rost_ves={'rost': input("input rost: "), 'ves':input("input ves: ")}
    print(rost_ves)
    name2=input("name: ")
    info2=dict.fromkeys([name2],rost_ves)
    return info2
info1=first_dict()
info2=second_dict()

print(info1)
print(info2)
if input(print("together?: "))=="y":
    info={}
    info=info1.copy()
    info.update(info2)
    for key,value in info.items():
        print(key,"--",value)

#tel=input("his number")
#sl1=dict.fromkeys([a],b)

#a=input("name")
#b=input("his number")
#sl2=dict.fromkeys([a],b)



#for key in sl1.keys():
 #   sl2[key]=input("input email  ",get.keys(sl1))

#print(sl2)

