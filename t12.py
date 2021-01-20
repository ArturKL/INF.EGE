from random import shuffle


class Drawer:
    def __init__(self, *args):
        self.coords = list(args)

    def move(self, *args):
        for n, arg in enumerate(args):
            self.coords[n] += arg

    def get(self):
        return self.coords


def drawer():
    for a in range(0, 100):
        for b in range(0, 100):
            for c in range(0, 100):
                d = Drawer(0, 0, 2)
                d.move(4, 8, 10)
                for i in range(4):
                    d.move(2, -4, -5)
                    d.move(a, b, c)
                if d.get() == [24, 16, 12]:
                    return a, b, c


def editor():
    e = shuffle(('1' * 50) + ('2' * 50) + ('3' * 50))
    while e.find('12') or e.find('32') or e.find('31'):
        if e.find('12'):
            e.replace('12', '21')
