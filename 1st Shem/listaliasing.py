# Membership in lists
x=[10,20,30,40,50,60,70,80,90]
a=70
print(a in x)
# List aliasing 
a=[10,20,30,40,50,60,70]
b=a #aliasing operator # b is aliased in y
print(a)
print(b)
b[1]=99
print(a)
print(b)
# List cloning 
x=[10,20,30,40,50,60,70,80]
y=x[:] # : this is cloning operator and x is cloned y
print(x)
print(y)
x[0]=90
print(x)
print(y)
