for row in range(0,10):
    for col in range(0,10):
        if ((col==0 or col==9) or (row==col )):
            print("N ",end="")
        else:
            print("  ",end="")
    print()