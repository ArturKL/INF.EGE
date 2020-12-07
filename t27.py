f = open('27-B.txt', 'r')
n = int(f.readline())
s = 0
min_dif_with_1_left = None
second_min_dif_with_1_left = None
min_dif_with_2_left = None

for i in f.readlines():
    x, y = map(int, i[:-1].split(' '))
    diff = abs(x - y)
    if diff % 3 == 1:
        if min_dif_with_1_left is None or min_dif_with_1_left > diff:
            second_min_dif_with_1_left = min_dif_with_1_left
            min_dif_with_1_left = diff
    elif diff % 3 == 2:
        if second_min_dif_with_1_left is None or min_dif_with_2_left > diff:
            min_dif_with_2_left = diff
    s += min(x, y)
print(s)
if s % 3:
    if (s - min_dif_with_1_left) % 3 == 0:
        s -= min_dif_with_1_left
    else:
        s1 = 0
        if second_min_dif_with_1_left:
            s1 = s - second_min_dif_with_1_left - min_dif_with_1_left
        s2 = s - min_dif_with_2_left
        if s1:
            if s1 < s2:
                s = s1
            else:
                s = s2
        else:
            s = s2
print(s, min_dif_with_1_left, second_min_dif_with_1_left)
