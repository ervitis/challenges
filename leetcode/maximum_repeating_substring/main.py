"""
For a string sequence, a string word is k-repeating if word concatenated k times is a substring of sequence. The word's maximum k-repeating value is the highest value k where word is k-repeating in sequence. If word is not a substring of sequence, word's maximum k-repeating value is 0.

Given strings sequence and word, return the maximum k-repeating value of word in sequence.
"""


def max_repeating(sequence: str, word: str) -> int:
    if len(sequence) < len(word):
        return 0
    c = 0

    for i in range(101):
        if word*i in sequence:
            c = i
        elif len(sequence) < i:
            break
    return c


if __name__ == '__main__':
    print(max_repeating('a', 'a'))
    print(max_repeating('ababc', 'ab'))
    print(max_repeating('ababc', 'ba'))
    print(max_repeating('ababc', 'ac'))
    print(max_repeating('ababc', 'ba'))
    print(max_repeating("aaabaaaabaaabaaaabaaaabaaaabaaaaba", "aaaba"))
