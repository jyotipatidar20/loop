i=0
while i<=6:
    j=1
    while j<=6-i:
        print(" ",end=" ")
        j=j+1
    k=1
    while k<=6-j+i:
        print("*",end=" ")
        k=k+1
    print(" ")
    i=i+1