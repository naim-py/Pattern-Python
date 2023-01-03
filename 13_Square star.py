a = int(input("Enter the input for line = "))
for row in range(0,a):
    for col in range(0,a):
        if(col==0 or col==4 or ((row==0 or row==4 ) and (col>0 or col<4))) :
            print("* ",end="")

        else:
            print("  ",end="")
    print()