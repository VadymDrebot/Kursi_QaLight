def count_letter(x,y):
    count=0
    for item in range(len(x)):
        if x[item]==y:
            count+=1
    return count

spisok=str(input("input string:  "))
letter=input("input letter:  ")
print("There is(are) ",count_letter(spisok,letter), " times")