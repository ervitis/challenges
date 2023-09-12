"""
https://leetcode.com/problems/reverse-words-in-a-string/?envType=study-plan-v2&envId=top-interview-150
"""


def reverse_words(s: str) -> str:
    return ' '.join(reversed(s.strip().split()))


def main():
    print(reverse_words('the sky is blue'))
    print(reverse_words('  hello    world    '))


if __name__ == '__main__':
    main()
