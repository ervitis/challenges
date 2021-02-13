"""
At a lemonade stand, each lemonade costs $5.

Customers are standing in a queue to buy from you, and order one at a time (in the order specified by bills).

Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill.  You must provide the correct change to each customer, so that the net transaction is that the customer pays $5.

Note that you don't have any change in hand at first.

Return true if and only if you can provide every customer with correct change.
"""
from typing import List


def lemonade_change(bills: List[int]) -> bool:
    money = {5: 0, 10: 0, 20: 0}

    for bill in bills:
        money[bill] += 1
        charge = bill - 5
        if charge != 0:
            if charge == 5:
                if money[charge] != 0:
                    money[charge] -= 1
                else:
                    return False
            if charge == 15:
                if money[10] >= 1 and money[5] >= 1:
                    money[10] -= 1
                    money[5] -= 1
                elif money[5] >= 3:
                    money[5] -= 3
                else:
                    return False
    return True


if __name__ == '__main__':
    print(lemonade_change([5, 5, 5, 10, 20]))
    print(lemonade_change([5, 5, 10]))
    print(lemonade_change([10, 10]))
    print(lemonade_change([5, 5, 10, 10, 20]))
