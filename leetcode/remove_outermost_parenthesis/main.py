"""
A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.

Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.
"""


def remove_outer_parentheses(S: str) -> str:
    if len(S) == 0:
        return ''

    r = ''
    c = 0
    for s in S:
        if s == '(':
            c += 1
            if c > 1:
                r += s
        elif s == ')':
            c -= 1
            if c > 0:
                r += s
    return r


if __name__ == '__main__':
    print(remove_outer_parentheses('(()())(())'))
    print(remove_outer_parentheses('(()())(())(()(()))'))
    print(remove_outer_parentheses('()()'))
