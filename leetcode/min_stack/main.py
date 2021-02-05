"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    getMin() -- Retrieve the minimum element in the stack.

"""


class MinStack(object):

    def __init__(self):
        self.data = list()
        self.min_el = list()

    def push(self, x: int) -> None:
        self.data.append(x)
        if len(self.min_el) == 0 or x <= self.min_el[-1]:
            self.min_el.append(x)

    def pop(self) -> None:
        x = self.data.pop()
        if x == self.min_el[-1]:
            self.min_el.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.min_el[-1]


if __name__ == '__main__':
    obj = MinStack()
    obj.push(4)
    obj.pop()
    param_3 = obj.top()
    param_4 = obj.getMin()
