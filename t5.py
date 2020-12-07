def alg(n):
    a = n
    b = ''
    while n > 0:
        b = str(n % 2) + b
        n = n // 2
    summ = 0
    for dig in b:
        summ += int(dig)
    if summ % 2:
        b += '10'
    else:
        b += '00'
    r = int(b, 2)
    return r



for i in range(1, 10000):
    print(i, alg(i))