totalrows=int(input("Enter how many rows do you want to be print : "))

#Print Rows in dissanding order in right side
for rows in range(totalrows,0,-1):
    for symbol in range(1,rows+1):
        print("x",end=" ")
    print()

#Print Rows in dissanding order in left side
for rows in range(totalrows,0,-1): 
    for space in range(1,(totalrows-rows)+1):
        print(" ",end=" ")
    for symbol in range(1,rows+1):
        print("x",end=" ")
    print()
