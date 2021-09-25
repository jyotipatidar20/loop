n=int(input("enter the number"))
i=1
a=65
while i<n:
    j=1
    while j<i:
        print("",end="")
        j=j+1
    k=1
    while k<(n+i) :
        print(chr(a),end=" ") 
        k=k+1
        a=a+1
    print(" ")
    i=i+1