a = [1]
for i in range(2, 66):
    x = a[i - 2]
    if (i % 3 == 0 and i < 20) or (i % 3 == 0 and i / 3 >= 20):
        x += a[i // 3 - 1]
    a.append(x)
print(a[-1])
