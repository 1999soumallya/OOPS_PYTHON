list1=[10,20,30,40,50,60]
i=0
while i<len(list1):
    print(list1[i])
    i=i+1
for i in range(0,len(list1)):
    print(list1[i],end=" ")
    i=i+1

list2=[10,20,30,40,50]
print(list2)
list2.append(60)
print(list2)
list2[1:3]=25,35
print(list2)
