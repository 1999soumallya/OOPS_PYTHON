def selectionsort(ll):
    for i in range(len(ll)):
        min_index=i
        for j in range(i+1,len(ll)):
            if ll[min_index]>ll[j]:
                min_index=j
        ll[i],ll[min_index]=ll[min_index],ll[i]
        print("Sorted array",i+1,ll)

ll=[55,11,66,33,88,44]
selectionsort(ll)