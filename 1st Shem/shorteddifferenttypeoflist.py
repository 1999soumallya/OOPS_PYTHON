emp=[]
n=int(input("How many employee? "))

for i in range(n):
    print("Enter ID",end=" ")
    emp.append(input())
    print("Enter Name",end=" ")
    emp.append(input())
    print("Enter Salary",end=" ")
    emp.append(input())
print("The list is created with employee data")
id=int(input("Enter employee id: "))
for i in range(len(emp)):
    if id==emp[i]:
        print('id={:d},Name={:s},Salary={:.2f}'.format(emp[i],emd[i+1],emp[i+2]))
        break
