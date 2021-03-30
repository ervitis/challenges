"""
Write a program to count the number of days between two dates.

The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.
"""


def days_between_dates(date1: str, date2: str) -> int:
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap = lambda x: (x % 400 == 0) or (x % 100 and x % 4 == 0)

    def f(date):
        y, m, d = map(int, date.split('-'))
        x = 365 * (y - 1971) + sum(map(leap, range(1971, y)))
        return x + sum(months[:m - 1]) + d + (m > 2 and leap(y))

    return abs(f(date1) - f(date2))


if __name__ == '__main__':
    print(days_between_dates('2019-06-29', '2019-06-30'))
    print(days_between_dates('2020-01-15', '2019-12-31'))
