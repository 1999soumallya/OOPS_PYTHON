S=int(input("Enter The Value Of Starting Point: "))
E=int(input("Enter The Value Of Ending Point: "))
for num in range(S,E):
    if num%2==0:
        print(num,end=" ")
