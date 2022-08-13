def Selection_Sort(ll):
    for i in range(len(ll)-1):
        min_index=i
        for j in range(i+1,len(ll)):
            if ll[min_index]>ll[j]:
                min_index=j
        ll[i],ll[min_index]=ll[min_index],ll[i]
        print("Shorted Array : ",i+1,ll,)
lst = []
size = int(input("Enter size of the list: "))
for i in range(size):
    elements = int(input("Enter the element of the list: "))
    lst.append(elements)
Selection_Sort(lst)
