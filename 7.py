n=int(input("enter the number"))
i=1
while i<n:
    if i%2!=0:
        print("Weird")
    else:
        if (n>=2 and n<=5):
          print("Not weird")
        elif (n>=6 and n<=20):
           print("weird")
        elif i>20:
           print("not a weird")
        i=i+1
