count=1
while count<=100:
    if count%3==0:
        print("nav")
    elif count%7==0:
        print("gurukul")
    elif count%3==0 and count%7==0:
        print("navgurukul")
    else:
        print(count)
    count=count+1