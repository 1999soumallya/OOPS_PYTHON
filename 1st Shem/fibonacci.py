'''num=int(input("Enter the number n: "))
a=0
b=1
sum=0
print("The fibonacchi serice of the given number is: ")
for i in range(0,num):
    print(sum,end=" ")
    a=b
    b=sum
    sum=a+b'''

def recur_fibo(n):
    if(n<=1):
        return n
    else:
        return recur_fibo(n-1)+recur_fibo(n-2)
print(recur_fibo(5))
""""T(n)=T(n-1)+T(n-2)+2
T(0)="""