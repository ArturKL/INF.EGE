a = 3 * 10 ** 10
b = 5 * 10 ** 10
c = 0
minn = None
for i in range(a, b + 1, 100000):
    if (not i % 11) and (not i % 100000) and i % 17 and i % 23 and i % 41 and i % 103:
        c += 1
        if minn is None:
            minn = i
print(c, minn)