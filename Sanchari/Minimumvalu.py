import math


def minimum(arr, n):
    val = 0
    ans = 0
    for i in range(n):
        val += (math.log(arr[i]))
    left = 0
    right = arr[n-1]+1
    while left <= right:
        mid = (left+right)//2
        temp = n * (math.log(mid))
        if val < temp:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    print(ans)


n = int(input('Enter the size of an array: '))
arr = []
for i in range(0, n):
    N = int(input())
    arr.append(N)

minimum(arr, n)
