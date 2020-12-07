f = open('26.txt', 'r')
nums = [int(i) for i in f.readlines()]
more = list(sorted(filter(lambda x: x > 100, nums)))
less = filter(lambda x: x <= 100, nums)
summ = sum(less)
new_more = []
biggest_disc = None
for i in range(len(more) // 2):
    if biggest_disc is None:
        biggest_disc = more[i]
    elif biggest_disc < more[i]:
        biggest_disc = more[i]
    new_more.append(more[i] * 0.70)
    new_more.append(more[-i - 1])
print(new_more[-2])
new_more.append(len(more) // 2 + 1)
summ += sum(new_more)
print(summ, biggest_disc)