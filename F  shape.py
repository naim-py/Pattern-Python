for row in range(0,7):
    for col in range(0,5):
        if((col==0) or (row==0 or row==3)):
            print("* ",end="")
        else:
            print("  ",end="")
    print()
