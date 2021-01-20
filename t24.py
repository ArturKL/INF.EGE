from string import ascii_letters
f = open('24.txt', 'r')
ans = 0
c = 0
for i in f.readline():
    if i in ascii_letters:
        c += 1
    elif c >= 5:
        ans += 1 + (c - 5)
        c = 0
print(ans)