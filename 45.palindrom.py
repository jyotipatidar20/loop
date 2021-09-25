a=int(input("enter the numbere"))
b=a 
i=0
while a>0:
    i=(i*10)+a%10
    a//=10
    # i=i+1
if b==i:
    print("palindrom")
else:
    print("not palindrom")



