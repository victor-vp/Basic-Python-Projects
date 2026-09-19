import pickle
def append():
    try:
        f=open('flights.dat','rb+')
        s=pickle.load(f)
        while True:
            fid=int(input('enter flight id'))
            fname=input('enter flight name')
            n=int(input('enter no of passengers'))
            p=[fid,fname,n]
            s.append(p)
            ans=input('continue?')
            if ans in 'Nn':
                break
            else:
                pass
        f.seek(0)
        pickle.dump(s,f)
        f.close()
    except:
        f=open('flights.dat','wb')
        d=[]
        pickle.dump(d,f)
def delete():
    f=open('flights.dat','rb+')
    t=pickle.load(f)
    k=int(input('enter flight id to be deleted'))
    for i in t:
        if i[0]==k:
            t.remove(i)
            print('successfully removed')
        else:
            print('flight not found')
    f.seek(0)
    pickle.dump(t,f)
    f.close()
def display():
    f=open('flights.dat','rb')
    u=pickle.load(f)
    print('fid\t fname\t number')
    for j in list(u):
        print(j[0],'\t',j[1],'\t',j[2])
def menu():
    while True:
        print('''
1. create/append
2. delete
3. display''')
        ch=int(input('enter choice'))
        if ch==1:
            append()
        if ch==2:
            delete()
        if ch==3:
            display()
        ans=input('continue??')
        if ans in 'Nn':
            break
        else:
            pass
menu()
        
        
