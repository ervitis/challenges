"""
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.
"""
from collections import Counter


def can_construct(ransom_note: str, magazine: str) -> bool:
    cr = Counter(ransom_note)
    cm = Counter(magazine)

    for k in cr.keys():
        if cr[k] > cm[k]:
            return False
    return True


if __name__ == '__main__':
    print(can_construct('a', 'b'))
    print(can_construct('aa', 'aab'))
    print(can_construct('aab', 'baa'))
