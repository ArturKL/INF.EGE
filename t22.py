def alg(i):
    x = i
    a = 1
    while x > 0:
        a *= x % 7
        x = x // 7
    return a



print(alg(130), alg(131), alg(132))
for i in range(1, 10000):
    if alg(i) == 40:
        print(i, alg(i))
        exit()
