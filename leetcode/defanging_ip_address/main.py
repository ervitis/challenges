"""
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".
"""


def defang_ip_address(address: str) -> str:
    dia = ''
    for c in address:
        if c == '.':
            dia += '[.]'
        else:
            dia += c
    return dia


if __name__ == '__main__':
    print(defang_ip_address('255.100.50.0'))
