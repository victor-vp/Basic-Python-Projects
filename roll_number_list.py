l=[]
def create():
    while True:
        roll=int(input('enter roll nos'))
        l.append(roll)
        ans=input('continue? ')
        if ans in 'Nn':
            break
        else:
            pass
def findroll():
    for i in l:
        p=int(input('enter roll no to be checked'))
        if p == i:
            print('present')
        if p != i:
            print('Not present')
def menu():
    print('''
1. create list
2.search ''')
    while True:
        ch= int(input('enter choice'))
        if ch==1:
            create()
        elif ch==2:
            findroll()
        else:
            break
menu()
