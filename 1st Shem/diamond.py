totalrows=int(input("Enter how many number do yo want to be print : "))
for rows in range(1,totalrows):
    for space in range(1,(totalrows-rows)+1):
        print(" ",end=" ")
    for symbol in range(1,rows+1):
        print(" x ",end=" ")
    print()

for rows in range(totalrows,0,-1):
    for space in range(1,(totalrows-rows)+1):
        print(" ",end=" ")
    for symbol in range(1,rows+1):
        print(" x ",end=" ")
    print()
    
