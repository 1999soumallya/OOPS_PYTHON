def insertion_sort(ll):
    for i in range(1, len(ll)):
        temp = ll[i]
        j = i - 1
        while j >= 0 and ll[j] > temp:
            ll[j + 1] = ll[j]
            j = j - 1
        ll[j + 1] = temp
        print(f'After completing {i} pass: ')
        print(ll)


ll = [66, 33, 44, 11, 55, 22]
insertion_sort(ll)
