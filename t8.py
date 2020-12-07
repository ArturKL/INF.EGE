from itertools import product, permutations
combinations = list(map(lambda x: ''.join(x), product('БАЛКОН', repeat=5)))
print(combinations)
ans = []
for i in combinations:
    if 'Б' in i:
        ans.append(i)
print(len(ans), ans)
