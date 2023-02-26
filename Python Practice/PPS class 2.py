name=input("Enter Student's name: ")
print("Hello",name,"put your marks below:-")
E1=int(input("Marks in exam 1: "))
E2=int(input("Marks in exam 2: "))
S1=int(input("Marks in Sports Event: "))
A1=int(input("Marks in activity-1: "))
A2=int(input("Marks in activity-2: "))
A3=int(input("Marks in activity-3: "))
w1=.5*(E1+E2)/2
w2=.3*(S1)
w3=.2*(A1+A2+A3)/3
print("Students result: ",(w1+w2+w3),"percentage")


