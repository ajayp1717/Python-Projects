# #swapping
# a=2
# b=4
# a,b=b,a
# print (a)
# print(b)
# #new line :
# print("This is line 1\nThis is line 2\nThis is line 3")

#accept marks and calculate the percentage
import math
name=input("Enter ur name here: ")
print("hello ",name,"Enter marks of following subjects below")
Phy=int(input("Physics: "))
Che=int(input("Chem: "))
Mat=int(input("Maths: "))
Eng=int(input("English: "))
Comp=int(input("Computer: "))
average=(Phy+Che+Mat+Eng+Comp)/5
print("U have got ",average," percentage")
