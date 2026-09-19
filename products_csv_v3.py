import csv
def writing():
    try:
        f= open('products.csv','r+')
        prod=[]
        row=csv.writer(f)
        while True:
            a=int(input('enter product id'))
            b=input('enter the product name')
            c=int(input('enter the product quantity'))
            d=int(input('enter product price'))
            p=[a,b,c,d]
            prod.append(p)
            ans=input('continue??')
            if ans in 'Nn':
                break
            else:
                pass
        row.writerows(prod)
        f.seek(0)
        row=csv.reader(f)
        print(list(row))
        for i in row:
            print(i)
    except:
        f=open('products.csv','w')
        L=[]
        row=csv.writer(f)
        row.append(l)
def search():
    f= open('products.csv','r+')
    row=csv.reader(f)
    n=int(input('enter product id'))
    for i in row:
        if n==int(i[0]):
            print('found')
             print(i[0],i[1],i[2],i[3])
            
