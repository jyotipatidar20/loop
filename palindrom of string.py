
a=["mom","dad","radha","swati"]
d=[]
j=0
list=[]
while j<len(a):
    i=0
    b=str(a[j])
    c=""
    while i<len(b):
        c=b[i]+c
        i+=1
    if b==c:
        d.append(a[j])
    else:
        list.append(a[j]) 
    j=j+1
print(d)
print(list)





