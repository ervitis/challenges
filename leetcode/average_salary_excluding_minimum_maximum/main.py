"""
Given an array of unique integers salary where salary[i] is the salary of the employee i.

Return the average salary of employees excluding the minimum and maximum salary.
"""
from typing import List


def average(salary: List[int]) -> float:
    mi, ma = min(salary), max(salary)
    avg = 0
    c = 0
    for sal in salary:
        if sal != mi and sal != ma:
            avg += sal
            c += 1
    return avg / c


if __name__ == '__main__':
    print(average([4000, 3000, 1000, 2000]))
    print(average([1000, 2000, 3000]))
    print(average([6000, 5000, 4000, 3000, 2000, 1000]))
    print(average([8000, 9000, 2000, 3000, 6000, 1000]))
