from math import sqrt, floor, ceil


def divisors(num):
    ceiling = int(sqrt(num))
    divs = []
    if num == 1:
        return [1]
    for i in range(2, ceiling + 1):
        if num % i == 0:
            divs.append(i)
            div = num // i
            if i != div:
                divs.append(div)
    return divs
print(divisors(27))

x, y = 135790, 163228
for i in range(x, y + 1):
    dvs = divisors(i)
    s = sum(dvs)
    if s > 460000:
        print(len(dvs), s)