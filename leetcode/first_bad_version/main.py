"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
"""


def first_bad_version(n: int) -> int:
    def search(r0, r1):
        if isBadVersion(r0):
            return r0
        x = (r1 + r0) // 2
        if isBadVersion(x):
            return search(r0, x)
        if r1 - r0 == 1:
            return r1
        return search(x, r1)

    if n == 1:
        return n
    return search(1, n)


if __name__ == '__main__':
    print(first_bad_version(5))
