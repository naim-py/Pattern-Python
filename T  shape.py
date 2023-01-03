for row in range(0,7):
    for col in range(0,7):
        if((col==3) or (row==0)):
            print("* ",end="")
        else:
            print("  ",end="")
    print()