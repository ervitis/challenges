# -*- coding: utf-8 -*-

"""
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""


def pig_it(text):
    return ' '.join([t[1:] + t[:1] + 'ay' if t.isalpha() else t for t in text.split()])


def main():
    print(pig_it('O tempora o mores !'))
    print(pig_it('Hello world !'))


if __name__ == '__main__':
    main()
