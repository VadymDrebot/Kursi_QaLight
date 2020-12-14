
def symb_in_string(str,symb):
    it_list=[]
    count=0
    for i in range(len(str)):
        if str[i]==symb:
            it_list.append(i)
            count+=1
    return count, it_list

str_user=input("введите строку, в которой будем искать символ ")
symb_user=input("введите символ, в который будем искать в строке ")
count_user,user_list=symb_in_string(str_user,symb_user)
print("в стоке \t", str_user, "\nсимвол\t ",symb_user, "\nвстречаеться\t ",count_user , "раз(а)")
print(user_list)