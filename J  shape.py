for row in range(0,7):
    for col in range(0,6):
        if((col==3) or ((row == 0) and (col > 1 and col < 5)) or ((col==1) and(row==5 or row==6)) or(row==6 and col==2) ):
            print("* ",end="")
        else:
            print("  ",end="")
    print()