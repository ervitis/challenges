"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""


def climb_stairs(n: int) -> int:
    if n <= 2:
        return n

    st = [0] * (n+1)
    st[1] = 1
    st[2] = 2

    for i in range(3, n+1):
        st[i] = st[i-1] + st[i-2]
    return st[n]


if __name__ == '__main__':
    print(climb_stairs(2))
    print(climb_stairs(3))
    print(climb_stairs(6))
