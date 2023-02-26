def takedata():
    global x,y,choice
    x = float(input("enter first number: "))
    y = float(input("enter second number: "))
    choice=(input("Enter the operation to perform: "))
takedata()

def add(x,y):
    z = x + y
    return z
def sub(x,y):
    p = x - y
    return p
def mult(x, y):
    w = x * y
    return w
def div(x, y):
    q = x / y
    return q
if(choice=="Add"):
        print("Addition: ",add(x,y))
if(choice=="Sub"):
        print("Substraction: ",sub(x,y))
if(choice =="Mult"):
        print("Multiplication: ",mult(x,y))
if(choice =="Div"):
        print("Division: ",div(x,y))
