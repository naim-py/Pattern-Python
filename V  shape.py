for row in range(0, 5):
    for col in range(0, 5):
        if ((row==0 and (col==0 or col==4))or (row==1 and (col==1 or col==3))or (row==2 and (col==2 or col==2))):
            print("0 ", end="")
        else:
            print("  ", end="")
    print()
