import mysql.connector as x
import os

# Set your MySQL password as an environment variable instead of hardcoding it:
#   export DB_PASSWORD="your_password_here"
con = x.connect(
    host='localhost',
    password=os.environ.get('DB_PASSWORD', ''),
    user='root',
    database='test'
)
cur=con.cursor()
def insert():
    cur=con.cursor()
    q1='create table if not exists rolls(roll int, name varchar(25), tchrname varchar(25))'
    cur.execute(q1)
    con.commit()
    while True:
        cur=con.cursor()
        roll=int(input('enter roll no'))
        name=input('enter name of child')
        tchrname=input('name of teacher')
        q2=f"insert into rolls values ({roll},'{name}','{tchrname}')"
        cur.execute(q2)
        con.commit()
        ans=input('continue?')
        if ans in 'Nn':
            break
        else:
            pass
def deleterel():
    cur=con.cursor()
    n1=input('enter name to be deleted')
    q4=f"delete from rolls where name= '{n1}' "
    cur.execute(q4)
def new():
    cur=con.cursor()
    q5=f"select * from rolls "
    cur.execute(q5)
    r=cur.fetchall()
    for i in r:
        print(i)
    
    
        
 
    
