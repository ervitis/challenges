"""
A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.
"""
from collections import Counter


def check_if_pangram(sentence: str) -> bool:
    c = Counter(list('abcdefghijklmnopqrstuvwxyz'))
    for letter in list(sentence):
        c[letter] += 1
    return all([e >= 2 for e in c.values()])


def main():
    print(check_if_pangram('leetcode'))
    print(check_if_pangram('thequickbrownfoxjumpsoverthelazydog'))


if __name__ == '__main__':
    main()
