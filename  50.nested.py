# n=int(input("enter the number"))
i=1
while i<=5:
    j=1
    while j<=5-i:
        print(" ",end="")
        j=j+1
    k=1
    while k<i:
        print(k,end="")
        k=k+1
    l=i 
    while l>0:
        print(l,end="")
        l=l-1
    print(" ")
    i=i+1