totalrows=int(input("Enter how many rows do you wanted to print : "))
# Pint the triangle in right angle order
for row in range(1,totalrows+1):
    for symbol in range(0,row):
        print("x",end=" ")
    print()

# Pint the triangle in Left angle order
for row in range(1,totalrows+1):
    for space in range(1,(totalrows-row)+1):
        print(" ",end=" ")   
    for symbol in range(1,row+1):
        print("x",end=" ")
    print()
