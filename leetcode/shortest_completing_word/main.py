"""
Given a string licensePlate and an array of strings words, find the shortest completing word in words.

A completing word is a word that contains all the letters in licensePlate. Ignore numbers and spaces in licensePlate, and treat letters as case insensitive. If a letter appears more than once in licensePlate, then it must appear in the word the same number of times or more.

For example, if licensePlate = "aBc 12c", then it contains letters 'a', 'b' (ignoring case), and 'c' twice. Possible completing words are "abccdef", "caaacab", and "cbca".

Return the shortest completing word in words. It is guaranteed an answer exists. If there are multiple shortest completing words, return the first one that occurs in words.
"""
from collections import Counter
from copy import copy
from typing import List
import re


def shortest_completing_word(license_plate: str, words: List[str]) -> str:
    license_plate = license_plate.strip().lower()
    license_plate = re.sub(r'\s+', '', license_plate)
    license_plate = re.sub(r'\d', '', license_plate)
    count = Counter(license_plate)
    r = []

    for word in words:
        t = copy(count)
        wc = Counter(word)
        for k, v in wc.items():
            if k in t:
                t[k] -= v
        if all([e <= 0 for e in t.values()]):
            r.append((word, len(word)))

    m = min(r, key=lambda e: e[1]) if len(r) > 0 else ('', -1)
    return m[0]


if __name__ == '__main__':
    print(shortest_completing_word('1s3 PSt', ["step", "steps", "stripe", "stepple"]))
    print(shortest_completing_word('1s3 456', ["looks", "pest", "stew", "show"]))
    print(shortest_completing_word("GrC8950",
                                   ["measure", "other", "every", "base", "according", "level", "meeting", "none",
                                    "marriage", "rest"]))
    print(shortest_completing_word('OgEu755',
                                   ["enough", "these", "play", "wide", "wonder", "box", "arrive", "money", "tax",
                                    "thus"]))
