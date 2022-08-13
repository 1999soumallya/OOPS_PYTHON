a=int(input("Enter the number of a: "))
b=int(input("Enter the number of b: "))
def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
print("The gcd of a and b is : ",end=" ")
print(gcd(a,b))
