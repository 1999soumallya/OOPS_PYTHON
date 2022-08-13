startnumber=int(input("Enter the starting point of a serige: "))
endnumber=int(input("Enter the ending point of a serige: "))
print("The amstrong numbers are: ")
for i in range(startnumber,endnumber):
    order=len(str(i))
    temp=i
    sum=0
    while temp>0:
        degit=temp%10
        sum +=(degit**order)
        temp //=10
    if i==sum:
        print(i,end=" ")
