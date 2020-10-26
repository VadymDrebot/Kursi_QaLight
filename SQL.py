import sqlite3 as sq
with sq.connect("tabl1.db") as con:
    cur=con.cursor()
#создание первой таблицы
    cur.execute("DROP TABLE worker")
    cur.execute("""CREATE TABLE IF NOT EXISTS worker(id INTEGER PRIMARY KEY,surname TEXT,name TEXT)""")
    users=[(123,'ivanov','ivan'),(456,'petrov','petya'),(789,'sidorov','sidor')]
    cur.executemany("INSERT INTO worker VALUES(?,?,?)",users)
# создание второй таблицы
    cur.execute("DROP TABLE salary")
    cur.execute("""CREATE TABLE IF NOT EXISTS salary(id INTEGER PRIMARY KEY,per_month INTEGER,bonus INTEGER)""")
    salaries=[(123,3000,100),(456,4000,300),(789,5000,600)]
    cur.executemany("INSERT INTO salary VALUES(?,?,?)", salaries)
# создание третьей таблицы
    cur.execute("DROP TABLE position")
    cur.execute("""CREATE TABLE IF NOT EXISTS position(id INTEGER PRIMARY KEY,positions TEXT,experience_year TEXT)""")
    pos = [(123, 'director', '15'), (456, 'counter', '10'), (789, 'driver', '3')]
    cur.executemany("INSERT INTO position VALUES(?,?,?)", pos)

    cur.execute("""SELECT * FROM worker """)
    for i in cur:
        print(i)

    cur.execute("""SELECT * FROM salary """ )
    for i in cur:
        print(i)

    cur.execute("""SELECT * FROM position """)
    for i in cur:
        print(i)


    cur.execute("""SELECT surname,per_month FROM worker JOIN salary
                 ON worker.id==salary.id""")
    for i in cur:
        print(i)
