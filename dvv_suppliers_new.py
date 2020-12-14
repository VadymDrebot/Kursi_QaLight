from tkinter import *
from tkinter.ttk import Radiobutton

import sqlite3
con = sqlite3.connect("../raznoe/suppliers.db")
add = []
def click_button():
    if sel.get() == 1:
        create_tables()
    elif sel.get() == 2:
        out_suplliers()
    elif sel.get() == 3:
        out_supply_group()
    elif sel.get() == 4:
        add_item()
    elif sel.get() == 5:
        find_item()
    return
#   lbl.configure(text="работаем...")    # изменение надписи слева
###################################

def create_tables():
    cur = con.cursor()
    cur.execute("""DROP TABLE IF EXISTS suppliers""")
    cur.execute("""CREATE TABLE IF NOT EXISTS suppliers (
                    id TEXT PRIMARY KEY,surname TEXT,name TEXT,group_id INTEGER) """)
    users = [(12, 'ivanov', 'ivan', 48), (23, 'petrov', 'petr', 65), (45, 'sidorov', 'sidr', 48)]
    cur.executemany("""INSERT INTO suppliers VALUES(?,?,?,?)""", users)

    cur.execute("""DROP TABLE IF EXISTS supply_group""")
    cur.execute("""CREATE TABLE IF NOT EXISTS supply_group(
                        group_id INTEGER PRIMARY KEY,group_name)""")
    groups = [(48, 'global'), (65, 'local')]
    cur.executemany("""INSERT INTO supply_group VALUES(?,?)""", groups)
    con.commit()
    return
##################################
def out_suplliers():
    cur = con.cursor()
    cur.execute("""SELECT id,name,surname,group_id FROM suppliers """)
    a = 200
    for i in cur:
        lbl_create = Label(window, text=i)
        lbl_create.place(x=150, y=a)
        a += 20
    return
########################################
def out_supply_group():
    cur = con.cursor()
    cur.execute("""SELECT group_id,group_name FROM supply_group """)
    for a in range(200,550,10):
        lbl_create = Label(window, text="                              ")
        lbl_create.place(x=150, y=a)

    a = 200
    for i in cur:
        lbl_create = Label(window, text=i)
        lbl_create.place(x=150, y=a)
        a += 20
 #   con.commit()
    return
###########################################
def add_item():
    if len(add)<= 4:
        line = "id              "
        if len(add) == 0:
            line = "input name     "
        elif len(add) == 1:
            line = "input surname "
        elif len(add) == 2:
            line = "input id_group"
        input_lbl = Label(window, text=line)  # неактивна надпись слева
        input_lbl.place(x=20, y=10)
        txt = Entry(window, textvariable=message)  # ввод с клавиатуры
        txt.place(x=120, y=10)
        txt.focus()
        add.append(message.get())
        message.set("")

    if len(add) == 4:
        cur = con.cursor()
        cur.execute("""INSERT INTO suppliers (id,surname,name,group_id) VALUES (?,?,?,?)""",add)
        con.commit()
        input_lbl = Label(window, text='    DONE         ')
        input_lbl.place(x=20, y=10)

    else:
        return
##########################поиск  и вывод на экран работника по ID,name or surname
def find_item():
    txt = Entry(window, textvariable=message)  # ввод с клавиатуры
    txt.place(x=120, y=10)
    txt.focus()                                 # фокус на окно ввода при запуске

    cur = con.cursor()
    search =message.get()
    cur.execute("""SELECT id,surname,name FROM suppliers """)
    count = 0
    for el in cur:
        for i in range(3):
            if search == el[i]:
                lbl_create = Label(window, text="   Это:       ")
                lbl_create.place(x=150, y=300)
                lbl_create = Label(window,text= el)
                lbl_create.place(x=220, y=300)
                count = 1
    if count == 0:
        lbl_create = Label(window, text="we dont have such name")
        lbl_create.place(x=150, y=300)
    return
##########################
def delete():
    lbl = Label(window, text="удалить запись?")  # неактивна надпись слева
    lbl.grid(column=1, row=5)
    return


window = Tk()
window.title("Работа с базами данных")   # заголовок окна
window.geometry("500x400+600+400")       # ширина и высота окна со смещением
line = "Input data"
input_lbl = Label(window, text=line)  # неактивна надпись слева
input_lbl.place(x=20, y=10)

message = StringVar()
txt = Entry(window, textvariable=message)  # ввод с клавиатуры
txt.place(x=120, y=10)

txt.focus()  # фокус на окно ввода при запуске
search =message.get()  # message= значение из окна ввода


btn = Button(text=" OK ",command=click_button) # конструктор BUTTON
btn.place(x=350,y=10)

sel = IntVar()                          # переменная для хранения состояний виджетов
sel.set(0)                              # присваиваем для sel значение 0
rad1 = Radiobutton(window, text='Создать базы SUPPLIERS и SUPPLY_GROUP?',variable=sel,value=1)# sel.get()=1
rad2 = Radiobutton(window, text='Вывод базы SUPPLIERS   ',variable=sel,value=2)  # sel.get()=2
rad3 = Radiobutton(window, text='Вывод базы SUPPLY_GROUP',variable=sel,value=3)  # sel.get()=3
rad4 = Radiobutton(window, text='Добавить запись?      ',variable=sel,value=4)   # sel.get()=4
rad5 = Radiobutton(window, text='Найти запись?        ',variable=sel,value=5)    # sel.get()=5
rad1.place(x=10, y=50)
rad2.place(x=10, y=80)
rad3.place(x=10, y=110)
rad4.place(x=10, y=140)
rad5.place(x=10, y=170)

window.mainloop()                        #отображение окна#
con.close()
###########################################
