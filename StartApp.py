from Calculator import Calculator

calc = Calculator()

print("Select option / * + - ")
option = input()

print("Insert 2 numbers: ")
nr1 = int(input("nr1 = "))
nr2 = int(input("nr2 = "))

if option == "+":
    calc.summa(nr1, nr2)
elif option == "*":
    calc.umnojiti(nr1, nr2)
elif option == "/":
    calc.deliti(nr1, nr2)
elif option == "-":
    calc.minus(nr1, nr2)
else:
    print("Unknown option")