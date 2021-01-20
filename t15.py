def DEL(a, b):
    return not (a % b)


def f(a, x, y=0):
    return (DEL(x, a) and DEL(x, 16)) <= ((not DEL(x, 16)) or DEL(x, 24))


# ans = 0
# for A in range(1, 1000):
#     lose = False
#     for x in range(1, 1000):
#         if not f(A, x):
#             lose = True
#             break
#     if not lose:
#         print(A)
#         print(A, f(A, 3212314))
#         exit()
# print(ans)
for x in range(1, 1000000):
    if not f(3, x):
        print('sosi')