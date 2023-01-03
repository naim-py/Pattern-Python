a = int(input("Enter the input for line = "))
for i in range(0,a+1):
    for j in range(1,i+1):
        print("* ",end="")
    print()
for i in range((a-1),0,-1):# a=5,,5-1=4
    for j in range(1,i+1): #i=4+1=5,,,1,2,3,4
        print("* ",end="")
    print()
