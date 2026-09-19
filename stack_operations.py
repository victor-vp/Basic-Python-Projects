stack=[]
def push():
        o=int(input('enter item to be pushed in'))
        stack.append(o)
def pop():
    if len(stack)!=0:
        stack=stack.pop()
        print(stack)
def menu():
    print('''
1.push
2.pop ''')
    while True:
        ch=int(input('enter choice'))
        if ch==1:
            push()
        elif ch==2:
            pop()
        else:
            break
        ans=input('continue?')
        if ans in 'Nn':
            break
        else:
            pass
        
    
