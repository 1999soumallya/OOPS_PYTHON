num=int(input("Enter the number of n: "))

if num>1:
    for i in range(2,num):
        if(num%i)!=0:
            print(num," Is a prime number")
            break
        else:
            print(num," Is not a prime number")
            break
