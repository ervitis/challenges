"""
Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.
"""
from typing import List


def find_restaurant(list1: List[str], list2: List[str]) -> List[str]:
    c = set(list1) & set(list2)
    d = {}
    for k, v in enumerate(list1):
        if v in c:
            d[v] = k + 1
    for k, v in enumerate(list2[::-1]):
        if v in c:
            d[v] -= k + 1
    m = min(d.values())
    return [k for k, v in d.items() if v == m]


if __name__ == '__main__':
    print(find_restaurant(list1=["Shogun", "Tapioca Express", "Burger King", "KFC"],
                          list2=["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]))
