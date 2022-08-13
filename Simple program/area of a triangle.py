a=int(input("Enter the first side of a triangle: "))
b=int(input("Enter the second side of a triangle: "))
c=int(input("Enter the third side of a triangle: "))
s=(a+b+c)/2

c=(s*(s-a)*(s-b)*(s-c))-(1/2)

print("The area of a triangle is : ",c)
