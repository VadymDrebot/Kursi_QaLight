def sec_in_time(secund):
    day=0
    hour=0
    min=0
    sec=0

    sec=secund%60
    min=(secund//60)%60
    hour=( secund // (60*60) )%24
    day= secund // (60*60*24)

    return day, hour, min, sec

num_secund=int(input("введите секунды "))
d,h,m,s=sec_in_time(num_secund)
print("дней \t",d,"\tчасов \t",h,"\tминут \t",m,"\tсекунд \t",s)