for row in range(0,8):
    for col in range(0,10):
        if ((row==2 and col==1) or(row==3 and col==1) or(row==2 and col==5) or(row==3 and col==5) or((row==1 or row==4) and (col>1 and col <5))):
            print("* ",end="")
        else:
            print("  ",end="")
    print()