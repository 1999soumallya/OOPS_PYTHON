#1
string="Dr. B. C. Roy Engineering College, Durgapur"
k=[print(i) for i in string if i not in "aeiouAEIOU"]

#2
x=[i**+1 for i in range(3)];
print (x)

#3
print([i+j for i in "abc" for j in "def"])

#4
print([[i+j for i in "abc"]for j in "def"])

#5
l1=[1,2,3]
l2=[4,5,6]
k=[x*y for x in l1 for y in l2]
print(k)

#6
ll=[10,40,-50,-3,96]
print([x for x in ll if x<0])

#7
s=["pune","mumbai","delhi"]
print([(w.upper(),len(w))for w in s])

#8
l=[1,2,3,4,5,6,7,8,9]
print([x**3 for x in l])

#9
t=32.00
print([round((x-32)*5/9)for x in t])

#10
list1=[1,3,2]
list1*2

#11
names1=['Amir','Bala','Charlie']
names2=[name.lower()for name in names1]
print(names2[2][0])

#12
values=[[3,4,5,1],[33,6,1,2]]
v=values[0][0]
for lst in values:
    for element in lst:
        if v>element:
            v=element
print(v)

#13
A=[[1,2,3],[4,5,6],[7,8,9]]
print([A[i][len(A)-1-i]for i in range(len(A))])

#14
print([x for x in range(1,1000)if x%5==0])

#15
for i in range(1,101):
    if int(i*0.5)==i*0.5:
        print(i)

#16
print([i for i in range(1,101) if int(i*0.5)==(i*0.5)])

#17
print([(2**x) for x in range(0,13)])

#18
ll=[j for i in range(2,8) for j in range(i*2,50,i)]
print(ll)

#19
ll=[[1,2,3],[4,5,6],[7,8,9]]
print(ll[2][1])

#20
w="hello"
v=('a','e','i','o','u')
print([x for x in w if x in v])

#21
print([x for x in range(0, 20) if (x%2==0)])