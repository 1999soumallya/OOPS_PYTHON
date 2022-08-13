num=[10,20,30,40,50]
print("Total list = ",num)
print("First=%d,last=%d",(num[0],num[4]))
list1=['RAJU','VANI','GOPAL','LAXMI']
print("Total list = ",list1)
print("First=%d,last=%d",(list1[0],list1[3]))
list2=[10,20,10.5,2.55,'GANESH','VISHNU']
print("First=%d List=%d",(list2[0],list2[5]))

for i in range(0,10,1):
    print(i,end=" ")

lst=list(range(0,10,2))
print(lst)

list3=range(10)
for i in list3:
    print(i,",",end=" ")
list4=range(5,10)
for i in list4:
    print(i,",",end=" ")
list5=range(5,10,2)
for i in list5:
    print(i,",",end=" ")