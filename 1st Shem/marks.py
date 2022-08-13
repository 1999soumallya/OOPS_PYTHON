ll=[]
n=int(input("How many subjects ar exesit? "))
for i in range (n):
    print("enter the mark")
    ll.append(int(input()))

def marks(ll):
    total=sum(ll)
    print('The candidate obtende marks is :',total)
    avarage=total/n
    print('The candidate parcentege is :',avarage,"%")
    if avarage>=90.00:
        return 'Grade is A'
    elif avarage>=70.00:
        return 'Grade is B'
    elif avarage>=50.00:
        return 'Grade is C'
    else:
        return 'Candidate is fail'
m=marks(ll)
print(m)
'''def marks(m1,m2,m3,m4,m5):
    total=(m1+m2+m3+m4+m5)
    print('The candidate obtende marks is :',total)
    avarage=total/5
    print('The candidate parcentege is :',avarage,"%")
    if avarage>=90.00:
        return 'Grade is A'
    elif avarage>=70.00:
        return 'Grade is B'
    elif avarage>=50.00:
        return 'Grade is C'
    else:
        return 'Candidate is fail'
a,b,c,d,e=[int(x) for x in input("Enter the marks:").split()]
m=marks(a,b,c,d,e)
print(m)'''