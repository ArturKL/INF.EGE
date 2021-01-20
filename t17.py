a, b = 3721, 7752
ans = 0
minn = 7752
print(bin(3723))
for i in range(a, b + 1):
    n = sum(map(int, list(str(i))))
    if n % 3 == 0 and n % 8:
        if i < minn:
            minn = i
        ans += 1
print(ans, minn)
