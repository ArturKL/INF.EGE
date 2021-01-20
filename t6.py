def alg(i):
    s, k = 5, 0
    d = i
    while s < d:
        k += 2
        s += k
    return s

print(alg(138))
for i in range(-1000, 1000):
    if alg(i) == 161:
        print(i)
        exit()

