import csv
def create():
    with open('students.csv','w') as f:
        stu=[]
        row=csv.writer(f)
        while True:
            a= int(input('enter student id'))
            b=input('enter student name')
            c=int(input('enter fees'))
            d=input('enter class')
            k=[a,b,c,d]
            stu.append(k)
            ans=input('do u want to continue')
            if ans in 'Nn':
                break
            else:
                continue
            row.writerows(stu)
def search():
    with open('students.csv','r+')as f:
        row=csv.reader(f)
        while True:
            p=int(input('enter student id to be checked'))
            for i in row:
                if i[0]==p:
                    print(i[0],'\t',i[1],'\t',i[2],'\t',i[3])
                else:
                    print('wrong id')
            ans=input('do u want to continue searching')
            if ans in 'Nn':
                break
            else:
                pass
            f.seek(0)
            f.close()
def display():
    with open('students.csv','r') as f:
        row=csv.reader(f)
        for i in row:
            print(i[0],'\t',i[1],'\t',i[2],'\t',i[3])

def menu():
    print('''
1. input data
2. search data
3.display all
4. exit''')
    while True:
        ch=int(input('enter ur chouce'))
        if ch==1:
            create()
        elif ch==2:
            search()
        elif ch==3:
            display()
        else:
            ans=int(input('do u want to continue'))
            if ans in 'Nn':
                break
            else:
                pass
            
menu()
            
    
            
        
    
