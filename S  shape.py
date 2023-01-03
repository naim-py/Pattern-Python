for row in range(0,9):
    for col in range(0,4):
        if((row==1 or row==5) or (row==4 and col==3) or (row==2 and col==0) or ((row==3) and (col==1 or col==2))):
            print("* ",end="")
        else:
            print("  ",end="")
    print()