"""
You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.

Given the string command, return the Goal Parser's interpretation of command.
"""


def interpret(command: str) -> str:
    s = ''
    co = 0
    for c in command:
        if c == 'G':
            s += 'G'

        if c == '(':
            if command[co+1:co+2] == ')':
                s += 'o'
            else:
                s += 'al'
        co += 1
    return s


if __name__ == '__main__':
    print(interpret('G()(al)'))
    print(interpret('G()()()()(al)'))
    print(interpret('(al)G(al)()()G'))
