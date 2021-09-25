num=int(input("enter the number"))
i=num
sum=0
while num>0:
    a=num%10
    sum=sum+a
    num=num//10
if i%sum==0:
    print("harshad number")
else:
     print("not harshad number")