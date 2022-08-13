str=[]
n=int(input("How many string element do wo want to insert in string? "))

for i in range(n):
    print("Enter string:",end=" ")
    str.append(input())

s=input("Enter the string which is wanted to search : ")
str1=sorted(str)
for i in str1:
    print("sorted List: ",i)

for i in range(len(str)):
    if s==str[i]:
        print("Found at :",i+1)
print("Not Found")
