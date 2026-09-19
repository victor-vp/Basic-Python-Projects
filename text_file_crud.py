def make():
    f=open('untitled.txt','w')
    m=''
    f.write(m)
    f.seek(0)
    f.close()
make()

def create():
    f=open('untitled.txt','w')
    while True:
        k=input('enter names of students in X11 C')
        f.write(k)
        ans=input('do u wannna to continue')
        if ans in 'Nn':
            break
        else:
            pass
    f.seek(0)
    f.close()

def read():
    f=open('untitled.txt','r')
    x=f.readlines()
    for i in x:
        print(i)
    f.close()

def search():
    f=open('untitled.txt','r+')
    y=f.read()
    l=input('the name to be searched')
    for j in y:
        if  l in j:
            print('found')
        else:
            print('not found')
    f.seek(0)
    f.close()

def append():
    f=open('untitled.txt','a')
    o=f.readlines()
    s=input('name to be removed')
    u=input('name to be replaced')
    for i in o:
        if i in s:
            i.replace(u)
    f.close()
    
def menu():
    while True:
        print('''
1. create a file
2. read the objects of file
3.search someone
4. append a record''')
        ch=int(input('enter ur choice'))
        if ch==1:
            create()
        elif ch==2:
            read()
        elif ch==3:
            search()
        elif ch==3:
            append()
        else:
            print('wrong choice')
        ans=input('do u wannna continue')
        if ans in 'Nn':
            break
        else:
            pass
menu()



        
    
