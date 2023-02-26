def reverse(n):
    if(n<=-10):
        print("Enter a value greater than -10")
    elif(-10<n<10):
        print(n)
    else:
        a=str(n%10)
        print(a,end="")
        reverse(n//10)
reverse(int(input("Enter the number here: ")))


