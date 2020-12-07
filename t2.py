print('x y z w f')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (x == (not y)) <= ((x and w) == z)
                if not f:
                    print(x, y, z, w, 0)