'''def maximum(ll):
    max=ll[-1]
    for i in range(-1,-len(ll),-1):
        if ll[i]>max:
            max=ll[i]
    return max
ll=[87,12,74,56]
print(maximum(ll))'''

def maximum(x,y,z):
    if (x>=y) and (x>=z):
            max=x
    elif (y>=x) and (y>=z):
        max=y
    else:
        max=z
    return max
x=9
y=8
z=10
print(maximum(x,y,z))
