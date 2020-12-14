name=input("name: ")
tel=input("input tel: ")
email=input("input email: ")
tel_em={'tel':tel,'email':email}
print(tel_em)
info1=dict.fromkeys([name],tel_em)
print(info1)



rost_ves={'rost': input("input rost: "), 'ves':input("input ves: ")}
print(rost_ves)
info2=dict.fromkeys([name],rost_ves)
mix={}
choice=int(input("input info: "))
while choice!=0:

    if choice==1:
        mix['tel']=tel_em['tel']
    elif choice==2:
        mix['email']=tel_em['email']
    choice = int(input("input info: "))

print(mix)
#tel_ves={info1[name]['tel'],info2[name]['ves']}
#print(tel_ves)