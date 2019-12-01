print("Hello world")
def calc(*args) :
    if(args[2]=='+'):
        a = args[0]+args[1]
    elif(args[2]=='-'):
        a=args[0]-args[1]
    elif(args[2] == '*'):
        a= args[0]*args[1]
    elif(args[2]== '/'):
        a=args[0]/args[1]
    else:
        a = str(args[0])+str(args[1])
    return a
d = int(input('A'))
b = int(input('B'))
c = input('Cno sdelati')
print(calc(d,b,c))
