# -*- coding: utf-8 -*-


def generate_hashtag(s):
    return False if len(s) == 0 or len(s) > 140 else '#' + ''.join([c.capitalize() for c in s.split()])


def main():
    print(generate_hashtag('Do We have A Hashtag'))
    print(generate_hashtag('Codewars      '))
    print(generate_hashtag('c i n'))


if __name__ == '__main__':
    main()
