# -*- coding: utf-8 -*-


def valid_braces(string):
    stack_br = []

    for s in string:
        if s == '(':
            stack_br.append(s)
        elif s == '{':
            stack_br.append(s)
        elif s == '[':
            stack_br.append(s)

        elif s == ')':
            if len(stack_br) == 0 or stack_br[len(stack_br)-1] != '(':
                return False
            else:
                stack_br.pop()
        elif s == '}':
            if len(stack_br) == 0 or stack_br[len(stack_br)-1] != '{':
                return False
            else:
                stack_br.pop()
        elif s == ']':
            if len(stack_br) == 0 or stack_br[len(stack_br)-1] != '[':
                return False
            else:
                stack_br.pop()

    return len(stack_br) == 0


def main():
    print(valid_braces('(){}[]'))
    print(valid_braces('([{}])'))
    print(valid_braces('[(])'))


if __name__ == '__main__':
    main()

