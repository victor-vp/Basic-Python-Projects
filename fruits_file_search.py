def create():
    l=[]
    while True:
        p=input('enter names of fruits')
        l.append(p)
        ans=input('do u want to continue')
        if ans in 'Nn':
            break
        else:
            pass
    f=open('fruits.txt','w')
    f.write(str(l))
    f.close()
def read():
    f=open('fruits.txt','r')
    k=f.read()
    print(k)
    f.close()
def copy():
    global f1
    f=open('fruits.txt','r')
    t=f.readlines()
    f.close()
    f1=open('copy.txt','w')
    for i in t:
        if 'the' in i:
            f1.write(i.strip())
            f1.close()
        f1=open('copy.txt','r')
        print(f1.read())
        f1.close()
