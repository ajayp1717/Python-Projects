# function
# calci

# def takedata():
#     global x,y       #making local variables global.
#     x=int(input("enter first number: "))
#     y=int(input("enter second number: "))
#
# def add():
#     z=x+y
#     print("sum:",z)
# def sub():
#     z=x-y
#     print("sub: ",z)
# def mult():
#     z=x*y
#     print("mult: ",z)
# def div():
#     z=x/y
#     print("Div: ",round(z,3))   #rounding off to decimal places
# takedata()                      #calling the function
# div()

# Parameter
def takedata():
    global x,y,choice
    x = int(input("enter first number: "))
    y = int(input("enter second number: "))
    choice =(input("Enter the operation to perform: "))
takedata()                                         # giving a choice to the user.

def add(x,y):
    z = x + y
    return z                    # A function returns the value where fn is called
def sub(x,y):
    p = x - y
    return p
def mult(x, y):
    w = x * y
    return w
def div(x, y):
    q = x / y                                   # print("sum is: ",add(x,y),"\ndifference is: ",sub(x,y))
    return q
if(choice=="Add"):
        print("addition: ",add(x,y))
if(choice =="Sub"):
        print("Substraction: ",sub(x,y))
if(choice =="Mult"):
        print("Multiplication",mult(x,y))
if(choice =="Div"):
        print("Division",div(x,y))
