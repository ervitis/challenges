"""
Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

The words in paragraph are case-insensitive and the answer should be returned in lowercase.
"""
from collections import Counter
from typing import List


def most_common_word(paragraph: str, banned: List[str]) -> str:
    paragraph = paragraph.lower().translate({33: 32, 63: 32, 39: 32, 44: 32, 59: 32, 46: 32}).split()
    words = sorted([(k, v) for k, v in Counter(paragraph).items()], reverse=True, key=lambda x: x[1])
    return [w for w in words if w[0] not in banned][0][0]


if __name__ == '__main__':
    print(most_common_word('Bob. hIt, baLl', ['bob', 'hit']))
    print(most_common_word('Bob hit a ball, the hit BALL flew far after it was hit.', ['hit']))
    print(most_common_word('a.', []))
    print(most_common_word('a, a, a, a, b,b,b,c, c', ['a']))
