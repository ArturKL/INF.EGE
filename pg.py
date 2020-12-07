a = int('10000', 16)
b = int('FFFFF', 16)
ans = 0
chet = '02468ACE'

for i in range(a, b + 1):
    n = hex(i)[2:]
    good = True
    for j in range(1, 5):
        if n[j] in chet and n[j - 1] in chet or n[j] not in chet and n[j - 1] not in chet:
            good = False
            break
    if good:
        ans += 1
print(ans)