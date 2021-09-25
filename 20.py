n=20
i=0
while n%2!=0:
    print("weird")
if n%2==0 and n in range(2,5):
     print(" not weird")
elif n%2==0 and n in range(6,20):
    print("weird")
elif n%2==0 and n>20:
    print("not weird")
i=i+1
    