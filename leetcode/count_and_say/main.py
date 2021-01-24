"""
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

    countAndSay(1) = "1"
    countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.

To determine how you "say" a digit string, split it into the minimal number of groups so that each group is a contiguous section all of the same character.
Then for each group, say the number of characters, then say the character. To convert the saying into a digit string, replace the counts with a number and concatenate every saying.
"""


def count_and_say(n: int) -> str:
    if n == 1:
        return '1'
    if n == 2:
        return '11'

    r = '11'
    for i in range(3, n + 1):
        r += '$'
        l = len(r)
        count = 1
        t = ''
        for j in range(1, l):
            if r[j] != r[j-1]:
                t += str(count + 0)
                t += r[j - 1]
                count = 1
            else:
                count += 1
        r = t
    return r


if __name__ == '__main__':
    print(count_and_say(1))
    print(count_and_say(4))
    print(count_and_say(12))
