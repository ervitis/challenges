# -*- coding: utf-8 -*-


def bubble(sentence):
    d = list(sentence)
    for i in range(len(d) - 1):
        for j in range(i, len(d)):
            if ord(d[i]) > ord(d[j]):
                d[i], d[j] = d[j], d[i]
    return d


def main():
    print(bubble('dddddzzzzzaazabhgbkirsdwtrhgbjytbaajtyccbb'))


if __name__ == '__main__':
    main()
