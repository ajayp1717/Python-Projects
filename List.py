N=int(input("Enter no. of elements to be added in the list: "))
list=[]
for i in range(N):
    a=int(input("Enter the element: "))
    list.append(a)
maximum=max(list)
minimum=min(list)
summation=sum(list)
average=summation/N
print("Maximum of the list is: ",maximum)
print("Minimum of the list is: ",minimum)
print("Sum of the list elements is: ",summation)
print("Average of the list elements is: ",average)

