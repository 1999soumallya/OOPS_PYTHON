num=int(input("Enter the number of n: "))
fact =1
if num<0:
    print("Sorry factoria does not exist in negative number")
elif num==0:
    print("The factorial of a number 0 is 1")
else:
    for i in range(1,num+1):
        fact=fact*i
    print("factorial of",num,"is",fact)


def rec_factorial(n):
    if n==0:
        return 1
    else:
        return(n*rec_factorial(n-1))
print(rec_factorial(5))