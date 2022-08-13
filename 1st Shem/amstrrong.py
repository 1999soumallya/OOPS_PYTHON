num=int(input("Enter this number which is wanted to print in amstrong mode: "))
temp=num
order=len(str(num))
sum=0
while temp>0:
    digit=temp%10
    sum +=(digit**order)
    temp //=10
if num==sum:
    print(num," Is an amstrong number")
else:
    print(num,"Is not an amstrong number")
