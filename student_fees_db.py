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

def insert():
    cur=con.cursor()
    q2='create table if not exists students(rollno int , class varchar(25), fees int)'
    cur.execute(q2)
    con.commit()

    while True:
        a=int(input('enter roll no to be added'))
        b=input('enter class ')
        c=int(input('enter fees'))

        
        q1=f"insert into students values ({a}, '{b}' ,{c})"
        cur.execute(q1)
        con.commit()

        ans=input('do u wnat to continue inserting values')
        if ans in 'Nn':
            break
        else:
            pass

def display():
    cur=con.cursor()
    q3="select * from students "
    cur.execute(q3)
    p=cur.fetchall()
    for i in p:
        print(i[0],'\t',i[1],'\t',i[2])
    con.commit()

def remove():
    cur=con.cursor()
    while True:
        o=int(input('enter roll no of student to be deleted'))
        q4=f" delete from students where rollno={o}"
        cur.execute(q4)
        print('SUCCESSFULLY REMOVED')
        ans=input('do u want to continue removing')
        if ans in 'Nn':
            break
        else:
            pass

def menu():
    while True:
        print('''
1. insert entries

2. display entries 

3. delete entries

4. exit''')
        ch=int(input('''

enter your choice

'''))
        if ch==1:
            insert()
        elif ch==2:
            display()
        elif ch==3:
            remove()
        else:
            break
        ans=input('do u want to continue in menu ')
        if ans in 'Nn':
            break
        else:
            pass

menu()
        
            
