num=int(input("enter the number"))
b=sum 
# k=1
sum=0
while num: 
    i=1
    j=1
    a=num%10
    while i<=a:
        j=j*i
    i=i+1
    sum=sum+j
    num=num//10
if sum==b:
    print("strong number")
else:
    print("not strong number")



