import pickle

def create():
    f=open('binfile.dat','wb')
    rec=[]
    pickle.dump(rec,f)
    f.close()

def append():
    f=open('binfile.dat','rb+')
    s=pickle.load(f)
    while True:
        empid=int(input('employee id'))
        empname=input('enter employee name')
        empsalary=int(input('enter salary'))
        rec={empid:(empname,empsalary)}
        s.append(rec)
        ans=input('do u want to continue')
        if ans in 'Nn':
            break
        else:
            pass

        pickle.dump(s,f)
        f.close()

def display():
    f=open('binfile.dat','rb')
    s=pickle.load(f)
    for i in s:
        for empid,(empname,empsalary) in rec.items():
            print(f"id:{empid}:name:{empname},salary:{empsalary}")
def search():
    f=open('binfile.dat','rb+')
    s=pickle.load(f)
    l=dict(s)
    t=int(input('enter id to be searched'))
    for j in l:
        if i[0]==t:
            print(i)
        else:
            print('not found')

create()

def menu():
    while True:
        print('''
1. add objects
2.display
3.search ''')
        ch=int(input('enter ur choice'))
        if ch==1:
            append()
        elif ch==2:
            display()
        elif ch==3:
            search()
        else:
            print('wrong choice')
        ans=input('do u wat to continue')
        if ans in 'Nn':
            break
        else:
            continue

menu()
    
    
