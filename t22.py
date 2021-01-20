def alg(i):
    x = i
    l = 0
    m = 1
    while x > 0:
        l = x % 10 + m + l
        x //= 10
        m *= 10
    return l


for i in range(1, 1000):
    res = alg(i)
    print(i, alg(i))

