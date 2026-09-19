import csv
def append():
    try:
        f=open('contacts.csv','a')
        c=[]
        row=csv.writer(f)
        while True:
            n=input('name of contact')
            p=int(input('enter ph of contact'))
            m=[n,p]
            row.writerows(m)
            ans=input('do u wanna continue??')
            if ans in 'Nn':
                break
            else:
                pass
        f.seek(0)
    except:
        f=open('contacts.csv','w')
        u=[]
        row=csv.writer(f)
        row.writerows(u)
def count():
    k=open('contacts.csv','r')
    q=csv.reader(k)
    j=list(q)
    print('count',len(j))

def disp():
    i=open('contacts.csv','r')
    t=csv.reader(i)
    for a in t:
        if a:
            print(a)
def menu():
    print('''
1. append or create
2. count
3. display''')
    while True:
        ch=int(input('enter your choice'))
        if ch==1:
            append()
        elif ch==2:
            count()
        elif ch==3:
            disp()
        else:
            print('not found')
        ans=input('continue??')
        if ans in 'Nn':
            break
        else:
            pass
menu()
        
