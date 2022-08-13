from typing import Sized


x=[]
size=int(input("Enter the size of list: "))
for i in range(size):
    element=int(input("Enter the element of list: "))
    x.append(element)
print(x)
big=x[0]
small=x[0]
for i in range(1,size):
    if x[i]>big:
        big=x[i]
for i in range(1,size):
    if x[i]<small:
        small=x[i]

print("The maximum number is :",big)
print("The munimum number is :",small)
x.sort(reverse=False)
print(x)