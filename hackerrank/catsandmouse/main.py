# -*- coding: utf-8 -*-


CATA = 'Cat A'
CATB = 'Cat B'
MOUSE = 'Mouse C'


# catA, catB, mouse
def cat_and_mouse(x, y, z):
    if abs(z - x) < abs(z - y):
        return CATA
    elif abs(z - x) > abs(z - y):
        return CATB
    else:
        return MOUSE


def main():
    print(cat_and_mouse(1, 2, 3))
    print(cat_and_mouse(1, 3, 2))


if __name__ == '__main__':
    main()
