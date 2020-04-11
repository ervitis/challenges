# -*- coding: utf-8 -*-

"""
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""


def pig_it(text):
    r = []
    for t in text.split(' '):
        if t.isalnum():
            if len(t) == 1:
                r.append(t + 'ay')
            else:
                r.append(t[1:] + t[:-len(t)+1] + 'ay')
        else:
            r.append(t)
    return ' '.join(r)


def main():
    print(pig_it('O tempora o mores !'))
    print(pig_it('Hello world !'))


if __name__ == '__main__':
    main()
