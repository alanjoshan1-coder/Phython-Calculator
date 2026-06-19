def add():
    a=int(input("Enter num1"))
    b=int(input("Enter num2"))
    c=a+b
    print("The sum is",c)

def sub():
    s=int(input("Enter num 1"))
    h=int(input("Enter num2"))
    d=s-h
    print("The difference is ",d)

def mul():
    w=int(input("Enter num 1"))
    e=int(input("Enter num2"))
    r=w*e
    print("The product is",r)

def divb():
    r=int(input("Enter num 1"))
    t=int(input("Enter num2"))
    y=r/t
    print("The quotient is",y)
while True:
    ch=input(print("Enter 1.Addition 2.Subtraction 3.Multiplication 4.Division 5.Exit"))
    if ch=="1":
        add()
    if ch=="2":
        sub()
    if ch=="3":
        mul()
    if ch=="4":
        divb()
    elif ch=="5":
        break
