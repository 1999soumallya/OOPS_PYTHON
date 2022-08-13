
def selectionshort1(ll):
    for i in range(len(ll)-1):
        min_index=i
        for j in range(i+1,len(ll)):
            if ll[min_index]>ll[j]:
                min_index=j
        ll[i],ll[min_index]=ll[min_index],ll[i]
        print("The shorted array = ",i+1,ll)
    return ll

ll=[]
size=int(input("Enter the size of list :"))
for i in range(size):
    element=int(input("Enter the elements"))
    ll.append(element)
"""ll=[90,10,80,20,70,30,60,40,50]"""
selectionshort1(ll)