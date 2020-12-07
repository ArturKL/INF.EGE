def DEL(a, b):
    return not (a % b)


def pain(x, a):
    return x > a


def f(a, x, y=0):
    return (pain(x**2, 60) or (not pain(x, a))) and ((not pain(y**2, 90) or pain(y, A)))


ans = 0
for A in range(1, 1000):
    lose = False
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not f(A, x):
                lose = True
                break
        if lose:
            break
    if not lose:
        ans += 1
        print(A, f(A, 3212314))
print(ans)