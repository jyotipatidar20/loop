n=int(input("enter the number"))
i=1
a=65
while n>0:
    j=1
    while j<i:
        print("",end="")
        j=j+1
    k=1
    while k<(n+i) :
        print("*",end=" ") 
        k=k+1
    print(" ")
    n=n-1
    i=i+1