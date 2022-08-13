n=int(input("Enter the number of factorial number="))
a=0
b=1
Count=0
if n<0:
    print("Pleace enter positive number")
elif n==1:
    print(a)
else:
    print("Fibonaccy Serice")
    while Count<n:
        print(a)
        c=a+b
        a=b
        b=c
        Count+=1