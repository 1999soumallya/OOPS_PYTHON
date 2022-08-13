def maxGroup(n):
    m = []
    for i in range(0, n):
        ele = int(input())
        m.append(ele)
    return m


'''if n >= 2 * m:
    return n
if m >= 2 * n:
    return m
if (m + n) % 3 == 0:
    return (m + n) // 3
ans = (m + n) // 3
m = m % 3
n = n % 3

if m and n and (m + n) >= 3:
    ans += 1
    return ans'''


if __name__ == '__main__':
    n = int(input('Enter the value'))
    print(maxGroup(n))
