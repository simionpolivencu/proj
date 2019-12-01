from Calculator import Calculator

calc = Calculator()

print("Select option / * + - ")
option = input()

print("Please insert 2 numbers: ")
nr1 = int(input("Number 1 = "))
nr2 = int(input("Number 2 = "))

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