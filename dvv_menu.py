from tkinter import *
import sqlite3
from tkinter.ttk import Combobox
con = sqlite3.connect("../raznoe/suppliers.db")
m_window = Tk()
add=[]  # пустой список для добавления элементов

def clean_window():                         # очистка экрана
    for i in range(10,900,5):
        l=Label(m_window, text="                                                                                         "
            "                                                                                                          ")
        l.place(x=20, y=i)
    return
def create_students():
    cur = con.cursor()
    cur.execute("""DROP TABLE IF EXISTS students""")
    cur.execute("""CREATE TABLE IF NOT EXISTS students (
                    st_id TEXT PRIMARY KEY,surname TEXT,name TEXT,telefon TEXT) """)
    users = [('st_1', 'Иванов', 'Иван', '0671111111'), ('st_2', 'Петров', 'Петр','0672222222'), ('st_3', 'Сидоров', 'Сеня','0972154878'),
             ('st_4','Семенов','Ваня ','0683265458'), ('st_5','Васильков','Вася','0681259845'), ('st_6','Соколов','Федя','0502564875')]
    cur.executemany("""INSERT INTO students VALUES(?,?,?,?)""", users)
##########################
    cur.execute("""DROP TABLE IF EXISTS politeh""")
    cur.execute("""CREATE TABLE IF NOT EXISTS politeh(
                            fak_id TEXT PRIMARY KEY,fak_name,dekan)""")
    fakultets = [('fak_1','ФАВТ','Козловский'), ('fak_2', 'Экономический','Петровский'),('fak_3','Машиностроительный','Семановский')]
    cur.executemany("""INSERT INTO politeh VALUES(?,?,?)""", fakultets)
#########################
    cur.execute("""DROP TABLE IF EXISTS favt""")
    cur.execute("""CREATE TABLE IF NOT EXISTS favt(
                                favt_sp_id TEXT PRIMARY KEY,favt_sp_name,favt_number_of_groups,favt_number_of_students)""")
    f_list = [('f_sp_1', 'Программирование', '4','120'), ('f_sp_2', 'Комп. сети', '3','90'),
            ('f_sp_3', 'Безопастность', '2','60'),('f_sp_4', 'Кодитование','2','52')]
    cur.executemany("""INSERT INTO favt VALUES(?,?,?,?)""", f_list)
#################################
    cur.execute("""DROP TABLE IF EXISTS economic""")
    cur.execute("""CREATE TABLE IF NOT EXISTS economic(
                                ec_sp_id TEXT PRIMARY KEY,ec_sp_name,ec_number_of_groups , ec_number_of_students)""")
    ec_list = [('ec_sp_1', 'Бухгалтерия', '4', '150'), ('ec_sp_2', 'Внешняя экономика', '3', '80'),
            ('ec_sp_3', 'Торговля', '2', '62'), ('tc_sp_4', 'Экономика производства', '2', '46')]
    cur.executemany("""INSERT INTO economic VALUES(?,?,?,?)""", ec_list)
###################################
    cur.execute("""DROP TABLE IF EXISTS mashine""")
    cur.execute("""CREATE TABLE IF NOT EXISTS mashine(
                                    m_sp_id TEXT PRIMARY KEY , m_sp_name , m_number_of_groups , m_number_of_students)""")
    m_list = [('m_sp_1', 'Автопроектирование', '3', '120'), ('m_sp_2', 'Военная техника', '3', '76'),
               ('m_sp_3', 'Автомобилестроение', '2', '62'), ('m_sp_4', 'Сельскохозяйственная', '1', '48')]
    cur.executemany("""INSERT INTO mashine VALUES(?,?,?,?)""", m_list)



    con.commit()
    return

def view_students():     ############# просмотр всех студентов-----база STUDENTS
    clean_window()
    cur = con.cursor()
    cur.execute("""SELECT st_id,surname,name,telefon FROM students """)
    head=["ID","Фамилия","   Имя   ","Телефон"]
    b = 20
    for i in range(4):
        main_lbl = Label(m_window, text=head[i], font="Arial 12")
        main_lbl.place(x=b, y=50)
        b += 120
    a = 100
    for item in cur:
        b=20
        for i in range(4):
            main_lbl=Label(m_window, text=item[i],font="Arial 14")
            main_lbl.place(x=b, y=a)
            b+=120
        a += 30
    return

def view_fakultets():#################    просмотр факультетов  --- база POLITEH
    clean_window()
    cur = con.cursor()
    cur.execute("""SELECT fak_id,fak_name,dekan FROM politeh """)
    main_lbl=Label(m_window,text="факультеты ПОЛИТЕХА",font="Arial 18")
    main_lbl.place(x=160, y=10)
    head = ["ID", "Факультет", " Декан  "]
    b = 20
    for i in range(3):
        main_lbl = Label(m_window, text=head[i], font="Arial 12")
        main_lbl.place(x=b, y=70)
        b += 240
    a = 150
    for item in cur:
        b = 20
        for i in range(3):
            main_lbl = Label(m_window, text=item[i], font="Arial 12")
            main_lbl.place(x=b, y=a)
            b += 240
        a += 30
    return

def view_favt():#################    просмотр факультета ФАВТ
    clean_window()
    cur = con.cursor()
    cur.execute("""SELECT favt_sp_id ,favt_sp_name,favt_number_of_groups,favt_number_of_students FROM favt""")
    head = ["ID", "Название", " Кол-во групп","Кол-во студентов"]
    b = 20
    for i in range(4):
        main_lbl = Label(m_window, text=head[i], font="Arial 12")
        main_lbl.place(x=b, y=50)
        b += 200
    a = 150
    for item in cur:
        b = 20
        for i in range(4):
            main_lbl = Label(m_window, text=item[i], font="Arial 12")
            main_lbl.place(x=b, y=a)
            b += 200
        a += 30
    return

def view_economic():#################    просмотр факультета ФАВТ
    clean_window()
    cur = con.cursor()
    cur.execute("""SELECT ec_sp_id,ec_sp_name,ec_number_of_groups,ec_number_of_students FROM economic""")
    head = ["ID", "Название", " Кол-во групп","Кол-во студентов"]
    b = 20
    for i in range(4):
        main_lbl = Label(m_window, text=head[i], font="Arial 12")
        main_lbl.place(x=b, y=50)
        b += 200
    a = 150
    for item in cur:
        b = 20
        for i in range(4):
            main_lbl = Label(m_window, text=item[i], font="Arial 12")
            main_lbl.place(x=b, y=a)
            b += 200
        a += 30
    return

def view_mashine():#################    просмотр факультета ФАВТ
    clean_window()
    cur = con.cursor()
    cur.execute("""SELECT m_sp_id ,m_sp_name, m_number_of_groups , m_number_of_students FROM mashine""")
    head = ["ID", "Название", " Кол-во групп","Кол-во студентов"]
    b = 20
    for i in range(4):
        main_lbl = Label(m_window, text=head[i], font="Arial 12")
        main_lbl.place(x=b, y=50)
        b += 200
    a = 150
    for item in cur:
        b = 20
        for i in range(4):
            main_lbl = Label(m_window, text=item[i], font="Arial 12")
            main_lbl.place(x=b, y=a)
            b += 200
        a += 30
    return

def new_student():
    add_window=Toplevel()                       # создание дополнительного(дочернего) окна
    add_window.title("Работа с базами данных")  # заголовок окна
    add_window.geometry("350x250+700+500")
    def otmena_click():                    # закрытие окна ADD STRING без сохранения данных
        add_window.after(3, lambda: add_window.destroy())
    def add_click():                           # кнопка в окне ADD STRING--"добавления новой строки"
        for i in range(4):
            add.append(message[i].get())
        cur = con.cursor()
        cur.execute("""INSERT INTO students (st_id ,surname ,name ,telefon) VALUES (?,?,?,?)""", add)
        con.commit()
        add_window.after(3, lambda: add_window.destroy())  # закрытие окна через 3 млсек

    line = ["Введите ID","Введите фамилию: ","Введите имя:","Введите тел.:"]
    a=10
    for i in range(4):
        x = line[i]
        input_lbl = Label(add_window, text=x)               # неактивна надпись слева
        input_lbl.place(x=20, y=a)
        a+=30
    message1=StringVar()
    message2=StringVar()
    message3 = StringVar()
    message4 = StringVar()
    message=[message1,message2,message3,message4]
    a = 10
    for i in range(4):
        txt1 = Entry(add_window, textvariable=message[i])  # ввод с клавиатуры
        txt1.place(x=150, y=a)
        a+=30
    btn = Button(add_window, text="    OK    ", command=add_click)  # конструктор BUTTON
    btn.place(x=100, y=150)
    btn = Button(add_window, text="Отмена", command=otmena_click)  # конструктор BUTTON
    btn.place(x=165, y=150)

    add_window.mainloop()
    return

def delete_student():
    return

def find_student():
    add_window = Toplevel()  # создание дополнительного(дочернего) окна
    add_window.title("Поиск студента")  # заголовок окна
    add_window.geometry("400x250+700+500")
    def otmena_click():  # закрытие окна ADD STRING без сохранения данных
        add_window.after(3, lambda: add_window.destroy())



    def find_click():
        condition=combo.get()
        search = [find_mes.get(),]
        if condition=="ID":
            cur = con.cursor()
            cur.execute("""SELECT st_id ,surname ,name ,telefon FROM students WHERE st_id=?""",search)
            count = 0
            for el in cur:
                for i in range(4):
                    lbl_create = Label(add_window, text=el,font="Arial 14")
                    lbl_create.place(x=20, y=170)
                    count = 1
            if count == 0:
                lbl_create = Label(add_window, text="Такого студента нет в базе",font="Arial 14")
                lbl_create.place(x=20, y=170)

    combo = Combobox(add_window)
    combo['values'] = ("ID","Фамилии","Имени" ,"Номеру тел.")
    combo.current(0)                        # установите вариант по умолчанию
    combo.place(x=30,y=20)

    btn = Button(add_window, text="    OK    ", command=find_click)  # конструктор BUTTON
    btn.place(x=70, y=120)
    btn = Button(add_window, text="Отмена", command=otmena_click)  # конструктор BUTTON
    btn.place(x=140, y=120)

    find_mes = StringVar()
    txt = Entry(add_window, textvariable=find_mes)  # ввод с клавиатуры
    txt.place(x=30, y=60)
    add_window.mainloop()
    return

def main_window():
    global main_lbl
    m_window.title("Работа с базами данных")   # заголовок окна
    m_window.geometry("800x400+300+200")
    mainmenu = Menu(m_window)
    new_menu = Menu()
    edit_menu= Menu()
    view_menu= Menu()
    mainmenu.add_cascade(label="   FILE   ", menu=new_menu)
    new_menu.add_command(label="Новая база студентов", command=create_students)
    new_menu.add_command(label="Загрузить базу студентов")#, command=create_students)
    new_menu.add_separator()
    new_menu.add_command(label="Новый студент",command=new_student)
    new_menu.add_command(label="Новая группа")#,command=create_supply_group)

    mainmenu.add_cascade(label="   EDIT   ",menu=edit_menu)
    edit_menu.add_command(label="Изменить инфо студента")#,command=add_string)
    edit_menu.add_command(label="Изменить инфо факультете")
    edit_menu.add_separator()
    edit_menu.add_command(label="Удалить студента",command=delete_student)

    mainmenu.add_cascade(label="   VIEW   ",menu=view_menu)
    view_menu.add_command(label="Просмотреть всех студентов  ",command=view_students)
    view_menu.add_command(label="Просмотреть факультеты", command=view_fakultets)
    view_menu.add_separator()
    view_menu.add_command(label="Просмотреть Фавт", command=view_favt)
    view_menu.add_command(label="Просмотреть Экономический", command=view_economic)
    view_menu.add_command(label="Просмотреть Машиностроительный", command=view_mashine)
    view_menu.add_separator()
    view_menu.add_command(label="Найти студента",command=find_student)
    m_window.config(menu=mainmenu)
    main_lbl = Label(m_window, text="Добро пожаловать!!!", font="Arial 18")
    main_lbl.place(x=130, y=200)

    m_window.mainloop()
    return

main_window()
#   main_lbl.place_forget()
# window.after(3000, lambda: window.destroy())  # закрытие окна--3 сек