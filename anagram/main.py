# -*- coding: utf-8 -*-
from collections import defaultdict, Counter


def read_lines():
    with open('littledictionary.txt', 'r') as fp:
        for line in fp:
            yield line


def anagram(letters):
    letters = ''.join(letters.lower().split(' ')).strip()
    anagrams = set()
    letters_count = Counter(letters)

    for line in read_lines():
        word = ''.join(line.lower().strip())

        if not set(letters) - set(word):
            check = set()
            for k, v in Counter(word).items():
                if v <= letters_count[k]:
                    check.add(k)
            if check == set(word) and len(word) == len(letters):
                anagrams.add(word)

    return sorted(list(anagrams), key=lambda x: len(x))


def main():
    print(anagram('act'))
    print(anagram('real fun'))
    print(anagram('robed'))


if __name__ == '__main__':
    main()

