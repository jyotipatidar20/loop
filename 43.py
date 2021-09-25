num=int(input("enter the number"))
b=num
c=int(input("enter the number"))
i=0
sum=0
while num>0:
    a=num%10
    i=a**c
    sum=sum+i
    num//=10
    # sum=sum+i
    # i=i+1
if sum==b:
    print("armstrong")
else:
    print("not armstrong")
    # i=i+1