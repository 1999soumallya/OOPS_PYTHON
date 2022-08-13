totalrows=int(input("Enter the how many rows do you want to be print : "))
#Print the Left angle triangle
for rows in range(1,totalrows+1):
    for symbol in range(0,rows):
        print(symbol+1,end=" ")
    print()
#Print the Right angle triangle
for rows in range(1,totalrows+1):
    for space in range(1,(totalrows-rows)+1):
        print(" ",end=" ")
    for symbol in range(0,rows):
        print(symbol+1,end=" ")
    print()
#Print the left angle triangle desanding order
for rows in range(totalrows,0,-1):
    for symbol in range(0,rows):
        print(symbol+1,end=" ")
    print()
#Print the right angle triangle desanding order
for rows in range(totalrows,0,-1):
    for space in range(0,(totalrows-rows)):
        print(" ",end=" ")
    for symbol in range(0,rows):
        print(symbol+1,end=" ")
    print()
#Print a triangle
for rows in range(1,totalrows+1):
    for space in range(0,(totalrows-rows)):
        print(" ",end=" ")
    for symbol in range(0,rows):
        print(symbol+1,end=" ")
    print()
