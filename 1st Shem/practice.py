totalrows=int(input("Enter how many rows do you want to print : "))
for row in range(1,totalrows+1):
    for symbol in range(1,row+1):
        print("x",end=" ")
    print()
