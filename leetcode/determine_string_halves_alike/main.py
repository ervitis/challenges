"""
You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.
"""


def halves_are_alike(s: str) -> bool:
    n = len(s)

    def count(st: str) -> int:
        vowels = 'aeiouAEIOU'
        nv = 0
        for c in st:
            if c in vowels:
                nv += 1
        return nv

    return count(s[:n//2]) == count(s[n//2:])


if __name__ == '__main__':
    print(halves_are_alike('book'))
    print(halves_are_alike('textbook'))
    print(halves_are_alike('MerryChristmas'))
    print(halves_are_alike('AbCdEfGh'))
