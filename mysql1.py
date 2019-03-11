import mysql.connector as myc

'''
user=root
password=mysql
host=localhost
database=will create

#that object we create
mycurser=obj.curser()
mycurser.execute("all sql query they are not case sensetive")
'''

obj=myc.connect(
    user='root',
    password='',
    host='localhost',
    database='maism'
    )
a="Krishan"
b='Ajmer'
mycursor=obj.cursor()
#mycursor.execute("insert into student(id,name,place) values(2,'%s','%s')" %(a,b))
#mycursor.execute("update student set name='Ram' where id=1")
mycursor.execute("delete from student where id=1")
mycursor.execute("select * from student")
mycursor.execute("commit")

for i in mycursor:
    print(i)
#innob_force_recovery=1
