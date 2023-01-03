for row in range(0,8):
    for col in range(0,10):
        if ((col==1) or (row==1 and col==1) or(row==2 and col==1) or(row==1 and col==4) or(row==2 and col==4) or((row==0 or row==3) and (col>1 and col <4))):
            print("P ",end="")
        else:
            print("  ",end="")
    print()