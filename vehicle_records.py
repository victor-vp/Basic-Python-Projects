import pickle
def appending():
    try:
        binfile=open('vehicles.dat','rb+')
        s=pickle.load(binfile)
        while True:
            vid=int(input('enter vehicleid'))
            vname=input('enter vname')
            vmodel=input('enter model name')
            vcolor=input('enter colour')
            vprice=int(input('enter price'))
            m=[vid,vname,vmodel,vcolor,vprice]
            s.append(m)
            ans=input('do u wanna continue')
            if ans in 'Nn':
                break
            else:
                pass
        binfile.seek(0)
        pickle.dump(s,binfile)
        binfile.close()
    except:
        binfile=open('vehicles.dat','wb')
        L=[]
        pickle.dump(L,binfile)

def search():
    f= open('vehicles.dat','rb+')
    s1=pickle.load(f)
    v=int(input('enter id to be searched'))
    for i in s1:
        if v == i[0]:
            print('present')
            print(i[0],i[1],i[2],i[3],i[4])
def update():
    k=open('vehicles.dat','rb+')
    s2=pickle.load(k)
    u=int(input('enter id to be updated'))
    u1=int(input('enter new id'))
    u2=input('enter new  name')
    u3=input('enter new model')
    u4=input('enter colour')
    u5=int(input('enter new price'))
    o=[u1,u2,u3,u4,u5]
    for j in s2:
        if j[0]==u:
            j[0]=u1
            j[1]=u2
            j[2]=u3
            j[3]=u4
            j[4]=u5
    print(list(s2))
    
            
            
            
            
            
            
