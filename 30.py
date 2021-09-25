sum=0
avg=0
i=1
while i<=11:
    a=int(input("enter the number"))
    if a%5==0:
        sum=sum+a
        avg =sum/11
    i=i+1
print(avg)