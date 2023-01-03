a = int(input("Enter the input for line = "))
for i in range(a,0,-1):
    for k in range(0,a-i):
        print(" ",end="")
    for j in range(0,i):
        print("* ",end="")
    print()
