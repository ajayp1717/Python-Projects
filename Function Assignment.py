global N
N=int(input("Enter a no. : "))
def sqr(N):
    return N**2
def sqrt(N):
    return N**0.5
def cub(N):
    return N**3
def prime(N):
    if N> 1:
        for i in range(2,N):
            if (N% i) == 0:
                print(N, "is not a prime number")
                break
        else:
            print(N, "is a prime number")
    else:
        print(N, "is not a prime number")
def fac(N):
    if N==1:
        return 1
    else:
        return(N*fac(N-1))
print((       " 0-Square "
              " 1-Sqaure root "
              " 2-Cube "
              " 3-Prime/not prime "
              " 4-Factorial "))
choice=int(input("\nEnter a number corresponding to the operation to perform: "))
if choice==0:
    print(sqr(N),"is square of",N)
elif choice==1:
    print(sqrt(N),"is square root of",N)
elif choice==2:
    print(cub(N),"is cube of",N)
elif choice==4:
    print(fac(N),"is a factorial of",N)
elif choice == 3:
    print(prime(N))









