"""
Given a string s. You should re-order the string using the following algorithm:

    Pick the smallest character from s and append it to the result.
    Pick the smallest character from s which is greater than the last appended character to the result and append it.
    Repeat step 2 until you cannot pick more characters.
    Pick the largest character from s and append it to the result.
    Pick the largest character from s which is smaller than the last appended character to the result and append it.
    Repeat step 5 until you cannot pick more characters.
    Repeat the steps from 1 to 6 until you pick all characters from s.

In each step, If the smallest or the largest character appears more than once you can choose any occurrence and append it to the result.

Return the result string after sorting s with this algorithm.
"""


def sort_string(s: str) -> str:
    r = ''
    n = len(s)
    arr = [0] * 26

    for c in s:
        arr[ord(c) - ord('a')] += 1

    while n > 0:
        for i in range(26):
            if arr[i] > 0:
                r += chr(ord('a') + i)
                arr[i] -= 1
                n -= 1
        for i in range(25, -1, -1):
            if arr[i] > 0:
                r += chr(ord('a') + i)
                arr[i] -= 1
                n -= 1
    return r


if __name__ == '__main__':
    print(sort_string('aaaabbbbcccc'))
    print(sort_string('leetcode'))
    print(sort_string('ggggggg'))
    print(sort_string('spo'))
