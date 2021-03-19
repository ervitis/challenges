"""
Your friend is typing his name into a keyboard. Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard. Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.
"""
from collections import Counter


def is_long_pressed_name(name: str, typed: str) -> bool:
    if len(typed) < len(name):
        return False

    n = Counter(name)

    j = 0
    for i in range(len(typed)):
        if j < len(name) and typed[i] == name[j]:
            j += 1
            n[typed[i]] -= 1
        elif i > 0 and typed[i] == typed[i-1]:
            continue
        else:
            return False
    return sum(n.values()) == 0


if __name__ == '__main__':
    print(is_long_pressed_name('alex', 'aaleex'))
    print(is_long_pressed_name('saeed', 'ssaaedd'))
