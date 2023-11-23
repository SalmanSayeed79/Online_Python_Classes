n=int(input("please enter a number: "))
i=1
while(i<=n):
    j=1
    while (j<=n-i):
        print(" ",end="")
        j=j+1
    k=1
    while (k<=i):
        print("*",end=" ")
        k=k+1
    print()
    i=i+1
n=n-1
i=1
while(i<=n):
    j=1
    while (j<=i):
        print(" ",end="")
        j=j+1
    k=0
    while (k<=n-i):
        print("*",end=" ")
        k=k+1
    print()
    i=i+1