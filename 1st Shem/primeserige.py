a=int(input("Enter the number of starting point: "))
b=int(input("Enter the number of ending point: "))
for num in range(a,b):
    count = 0
    if num>1:
        for i in range(2,(num//2+1)):
            if(num%i)==0:
                count=count+1
                break
        if(count==0 and num!=1):
            print(num,end=" ")
