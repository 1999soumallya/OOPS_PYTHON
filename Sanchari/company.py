fact = [1]


def preComputeFact(n):
    for i in range(1, n + 1):
        fact.append((fact[i - 1] * i))


def countFriendsPairings(n):
    ones = n
    twos = 1
    ans = 0
    while ones >= 0:
        ans = ans + (fact[n] // (twos * fact[ones] * fact[(n - ones) // 2]))
        ones = ones - 2
        twos = twos * 2
    return ans


preComputeFact(1000)
n = 4
print(countFriendsPairings(n))
