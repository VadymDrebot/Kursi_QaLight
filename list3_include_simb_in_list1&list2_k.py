import random

def list_numb_random():
    rand_list=list()

    for i in range(0,10):
        r=random.randint(0,10)
        rand_list.append(r)

    return rand_list

def compare_list(n_list1,n_list2):
    n_list3=list()

    for x in n_list1:

        if x in n_list2:
            n_list3.append(x)
            n_list2.remove(x)

    return n_list3


num_list1=list_numb_random()
print("первый список \t",num_list1)
num_list2=list_numb_random()
print("второй список \t",num_list2)
num_list3=compare_list(num_list1,num_list2)
if len(num_list3)==0:
    print("совпадений нет")
else:
    print("третий список \t",num_list3)



