import math as math

def f_2st(a,b,c):
    discr = b**2 - 4 * a *c
    if discr > 0:
        x1 = (-b + math.sqrt(discr))/2 * a
        x2 = (-b -  math.sqrt(discr))/2 * a
        print(x1)
        print(x2)
    if discr == "0":
        x = -b / 2 * a
        print(x)
    if discr < 0:
        print("Net kornei na R")
a = int(input("Introduce a"))
b = int(input("Introduce b"))
c = int(input("Introduce c"))
f_2st(a,b,c)