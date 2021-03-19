"""
Every valid email consists of a local name and a domain name, separated by the '@' sign. Besides lowercase letters, the email may contain one or more '.' or '+'.

    For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.

If you add periods '.' between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name. Note that this rule does not apply to domain names.

    For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.

If you add a plus '+' in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered. Note that this rule does not apply to domain names.

    For example, "m.y+name@email.com" will be forwarded to "my@email.com".

It is possible to use both of these rules at the same time.

Given an array of strings emails where we send one email to each email[i], return the number of different addresses that actually receive mails.
"""
from typing import List


def num_unique_emails(emails: List[str]) -> int:
    domains = {}
    for email in emails:
        name, dom = email.split('@')
        name = name.replace('.', '')
        if '+' in name:
            i = name.index('+')
            name = name[:i]
        if dom in domains and name not in domains[dom]:
            domains[dom].append(name)
        else:
            domains[dom] = [name]
    c = 0
    for names in domains.values():
        c += len(names)
    return c


if __name__ == '__main__':
    print(num_unique_emails(
        ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]))
    print(num_unique_emails(["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]))
