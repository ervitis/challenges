"""
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.
"""


def backspace_compare(S: str, T: str) -> bool:
    S = list(S)
    T = list(T)

    def transform(s: str) -> str:
        if '#' not in s:
            return s

        i = 0
        while i < len(s):
            if s[i] == '#':
                if i == 0:
                    s = s[i+1:]
                else:
                    s = s[:i - 1] + s[i+1:]
                    i -= 1
            else:
                i += 1
        return s

    S = transform(S)
    T = transform(T)
    return S == T


if __name__ == '__main__':
    print(backspace_compare('ab#c', 'ad#c'))
    print(backspace_compare('ab##', 'c#d#'))
    print(backspace_compare('a##c', '#a#c'))
    print(backspace_compare("hd#dp#czsp#####", "hd#dp#czsp#######"))
    print(backspace_compare('a#c', 'b'))
