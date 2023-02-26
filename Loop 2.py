print("Squares of first 10 natural numbers")
print("                                    ")
for i in range(1,11):
    Square=i**2
    print('  Square of',i,"=",Square)
     #while loop
i=0
while(i<=10):
    print(i**2)
    i+=1

    #break and continue statements
i=0
while(i<=10):
    i+=1
    if(i==5):
        continue #will skip iteration for i==5
    print(i**3)
