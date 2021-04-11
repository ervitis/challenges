"""
Given a string s containing only lower case English letters and the '?' character, convert all the '?' characters into lower case letters such that the final string does not contain any consecutive repeating characters. You cannot modify the non '?' characters.

It is guaranteed that there are no consecutive repeating characters in the given string except for '?'.

Return the final string after all the conversions (possibly zero) have been made. If there is more than one solution, return any of them. It can be shown that an answer is always possible with the given constraints.
"""


def modify_string(s: str) -> str:
    chs = set(s)
    av = set()
    for ch in s:
        if ch == '?':
            if not av:
                av = set('abcdefghijklmnopqrstuvwxyz').difference(chs)
            s = s.replace(ch, av.pop(), 1)
    return s


if __name__ == '__main__':
    print(modify_string('ubv?w'))
    print(modify_string(
        "????????????????????????????????????????????????????????????????????????????????????????????????????"))
