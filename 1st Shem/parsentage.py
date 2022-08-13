str=input("Enter The marks :").split(' ')
marks=[int(num) for num in str]
sum=0
for x in marks:
    print(x)
    sum+=x
print("Total marks: ",sum)
n=len(marks)
parcentage=sum/n
print("Parcentage: ",parcentage)