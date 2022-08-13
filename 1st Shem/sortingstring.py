str=[] #Creating a empty string

n=int(input('How many number string?')) # Enter how many element do you wanted to insert

for i in range(n):
    print("Enter string:",end=" ") # Enter the element of string
    str.append(input()) # And store the insert value in empty string
# The sring is shorted using str1=sorted(str) code
str1=sorted(str)
print("Shorted list: ")
for i in str1:
    print(i)