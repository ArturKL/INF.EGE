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


a, b = 289123456, 389123456
x, y = ceil(sqrt(a)), floor(sqrt(b))
print(x, y)
for i in range(x, y + 1):
    dvs = divisors(i**2)
    # print(dvs)
    if len(dvs) == 3:
        print(i, dvs)