"""
You are given a string text of words that are placed among some number of spaces. Each word consists of one or more lowercase English letters and are separated by at least one space. It's guaranteed that text contains at least one word.

Rearrange the spaces so that there is an equal number of spaces between every pair of adjacent words and that number is maximized. If you cannot redistribute all the spaces equally, place the extra spaces at the end, meaning the returned string should be the same length as text.

Return the string after rearranging the spaces.
"""


def reorder_spaces(text: str) -> str:
    words = text.strip().split()
    ns = 0
    for c in text:
        if c == ' ':
            ns += 1

    if ns == 0:
        return text

    if len(words) <= 1:
        return text.strip() + ' ' * ns

    ss = ns // (len(words) - 1)
    rs = ns % (len(words) - 1)
    r = ''
    for word in words:
        r += word + ' ' * ss
    r = r.rstrip()
    if rs > 0:
        r += ' ' * rs
    return r


if __name__ == '__main__':
    print(reorder_spaces('  this   is  a sentence '))
    print(reorder_spaces(' practice   makes   perfect'))
    print(reorder_spaces('  walks  udp package   into  bar a'))
    print(reorder_spaces('a'))
    print(reorder_spaces('  hello'))
