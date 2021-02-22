"""
Given numBottles full water bottles, you can exchange numExchange empty water bottles for one full water bottle.

The operation of drinking a full water bottle turns it into an empty bottle.

Return the maximum number of water bottles you can drink.
"""


def num_watter_bottles(num_bottles: int, num_exchange: int) -> int:
    return num_bottles + (num_bottles - 1) // (num_exchange - 1)


if __name__ == '__main__':
    print(num_watter_bottles(15, 4))
    print(num_watter_bottles(5, 5))
