print("guessing game")
i=5
j=1
while j<=5 :
    a=int(input("enter the number"))
    if a==5:
        print("you win")
    elif a<=5:
        print("take a one chance")
    else:
        print("rest the game")
    j=j+1


