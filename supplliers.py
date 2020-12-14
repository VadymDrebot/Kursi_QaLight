import sqlite3

def searching(): ############## поиск  и вывод на экран работника по ID,name or surname
    search=input("input id,name or surname: ")
    cur.execute("""SELECT id,surname,name FROM suppliers """)
    count = 0
    for el in cur:
        try:
            a=int(search)
            if el[0]==a:
                print("this is: ",el[1],el[2])
                count = 1
        except:
            if search==el[1]:
                print("this is: ", el[2],"with ID: ",el[0])
                count = 1
            elif search==el[2]:
                print("this is: ", el[1],"with ID: ",el[0])
                count = 1
    if count==0:
        print("we dont have such name")
    return
##############################################################

con=sqlite3.connect("../raznoe/suppliers.db")
cur = con.cursor()
#####
cur.execute("""PRAGMA foreign_keys = ON""")
cur.execute("""DROP TABLE IF EXISTS suppliers""")
cur.execute("""DROP TABLE IF EXISTS supply_group""")
#cur.execute(""".headers on""")
#cur.execute(""".mode column""")
#########################       SUPPLY_GROUP
cur.execute("""CREATE TABLE IF NOT EXISTS supply_group(
                group_id INTEGER PRIMARY KEY,group_name)""")
groups = [(48, 'global'), (65, 'local')]
cur.executemany("""INSERT INTO supply_group VALUES(?,?)""", groups)
########################       SUPPLIERS
cur.execute("""CREATE TABLE IF NOT EXISTS suppliers (
                id INTEGER PRIMARY KEY,surname TEXT,name TEXT,group_id INTEGER NOT NULL,
                FOREIGN KEY (group_id) REFERENCES supply_group (group_id)) """)
users=[(12,'ivanov','ivan',48),(23,'petrov','petr',65),(45,'sidorov','sidr',48)]
cur.executemany("""INSERT INTO suppliers VALUES(?,?,?,?)""",users)
########################        SUPPLY_INFO
cur.execute("""CREATE TABLE IF NOT EXISTS supply_info(
                surname TEXT PRIMARY KEY,tel INTEGER, email TEXT)""")
info = [(48, 'global'), (65, 'local')]
cur.executemany("""INSERT INTO supply_group VALUES(?,?)""", groups)

#####
a=[78,'durov','dur',65]
cur.execute("""INSERT INTO suppliers VALUES(?,?,?,?)""",a)


cur.execute("""SELECT id,name,surname,group_id FROM suppliers """)
for i in cur:
    print(i)

cur.execute("""SELECT group_id,group_name FROM supply_group """)
for i in cur:
    print(i)




 #   cur.execute("""SELECT group_name,id,name,surname FROM  supply_group LEFT JOIN suppliers
  #              ON suppliers.group_id=supply_group.group_id  ORDER BY group_name""")
   # for i in cur:
   #     print(i)
#print("")
#searching()
con.commit()
con.close()



