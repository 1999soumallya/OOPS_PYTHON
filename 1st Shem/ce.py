def func(x,ans):
    if(x==0):
        return 0
    else:
        return func(x-1,x-ans)
print(func(2,0))

def f(x=100,y=100):
    return(x+y, x-y)
x,y=f(y=200,x=100)
print(x,y)

for i in [1,2,3,4][::-1]:
    print(i)

for i in range(2.0):
    print(i)


    
x="BCREC,DURGAPUR"
print("%56s",x)
