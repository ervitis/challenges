"""
You are given a string time in the form of hh:mm, where some of the digits in the string are hidden (represented by ?).

The valid times are those inclusively between 00:00 and 23:59.

Return the latest valid time you can get from time by replacing the hidden digits.
"""


def maximum_time(time: str) -> str:
    time = list(time)
    if time[0] == '?':
        time[0] = '2' if time[1] in ['?', '0', '1', '2', '3'] else '1'
    if time[1] == '?':
        time[1] = '3' if time[0] == '2' else '9'
    if time[3] == '?':
        time[3] = '5'
    if time[4] == '?':
        time[4] = '9'
    return ''.join(time)


if __name__ == '__main__':
    print(maximum_time('2?:?0'))
    print(maximum_time('0?:3?'))
    print(maximum_time('1?:22'))
    print(maximum_time('??:??'))
    print(maximum_time('?4:03'))
