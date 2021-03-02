"""
You are given an array items, where each items[i] = [typei, colori, namei] describes the type, color, and name of the ith item. You are also given a rule represented by two strings, ruleKey and ruleValue.

The ith item is said to match the rule if one of the following is true:

    ruleKey == "type" and ruleValue == typei.
    ruleKey == "color" and ruleValue == colori.
    ruleKey == "name" and ruleValue == namei.

Return the number of items that match the given rule.
"""
from typing import List


def count_matches(items: List[List[str]], rule_key: str, rule_value: str) -> int:
    if len(items) == 0:
        return 0

    match = 0

    RTYPE = 0
    RCOLOR = 1
    RNAME = 2

    for item in items:
        if rule_key == 'type' and item[RTYPE] == rule_value or rule_key == 'color' and item[RCOLOR] == rule_value or rule_key == 'name' and item[RNAME] == rule_value:
            match += 1
    return match


if __name__ == '__main__':
    print(count_matches([["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]],
                        'color', 'silver'))
    print(count_matches([["phone", "blue", "pixel"], ["computer", "silver", "phone"], ["phone", "gold", "iphone"]],
                        'type', 'phone'))
