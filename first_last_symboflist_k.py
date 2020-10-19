def first_last_elem(str_numb):

    list_numb=list()

    try:

        for i in str_numb:
            if int(i) in range(0,10):
                list_numb.append(i)

        print(list_numb)
        #print("первый элемент списка ",list_numb[0] )
        last_ind=len(list_numb)
        #print("последний элемент списка ", list_numb[last_ind-1])
        return list_numb[0], list_numb[last_ind-1]

    except:
        print("в последовательности есть не только числа")
        return 0, 0


s=input("введите последовательность чисел ")
first_i, last_i = first_last_elem(s)
print("первый элемент списка ",first_i )
print("последний элемент списка ", last_i)