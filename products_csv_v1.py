import csv
def writing():
    f=open('products.csv','w+')
    prod=[]
    row=csv.writer(f)
    while True:
        a=int(input('enter prod id'))
        b=input('enter prod nam')
        c=int(input('enter the prod quantity'))
        d=int(input('enter prod price'))
        ans=input('do u wanna continue')
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
