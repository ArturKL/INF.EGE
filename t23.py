a = [1]
for i in range(2, 21):
    x = a[i - 2]
    if (i % 2 == 0 and i <= 10) or (i % 2 == 0 and i / 2 >= 10):
        x += a[i // 2 - 1]
    a.append(x)
print(a)
