def f(n):
    if n == 0:
        return 1
    elif n > 0:
        return 2*f(1 - n) + 3*f(n - 1) + 2
    elif n < 0:
        return -1 * f(-1 * n)


print(f(23))