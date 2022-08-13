# Normal program
str=input("Enter the main string: ")
sub=input("Enter the sub string: ")
n=str.find(sub,0,len(str))
if n==-1:
    print("Sub String is not found")
else:
    print("Sub string found position is: ",n+1)

# Using Excepction handaling protocal

str=input("Enter the main string: ")
sub=input("Enter the sub string: ")

try:
    n=str.index(sub,0,len(str))
    n=str.find(sub,0,len(str))
except:
    print("Sub string is not found")
else:
    print("Sub string found posiction is :",n+1)

