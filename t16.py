def f(n):
    if n == 1:
        return 1
    elif n > 1 and n % 2:
        return n + f(n - 2)
    elif not n % 2:
        return n * f(n - 1)


print(f(40))