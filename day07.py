import re


def read_data(data: str):
    d = []
    for l in data.splitlines():
        d.append(re.split("(\[[a-z]*\])", l))
    return d


def count_ips(data: str):
    d = read_data(data)
    n = 0
    for r in d:
        if ip_check(r):
            n += 1
    return n


def ip_check(r: list) -> bool:
    c = False
    for p in r:
        if p[0] == "[":
            if abba_check(p):
                return False
        else:
            if abba_check(p):
                c = True
    return c


def abba_check(s: str) -> bool:
    for i in range((s[0] == "["), len(s) - 3):
        if s[i] == s[i + 3] and s[i + 1] == s[i + 2] and not s[i] == s[i + 1]:
            return True
    return False


def count_aba_ips(s: str):
    data = read_data(s)
    n = 0
    for d in data:
        n += aba_check(d)
    return n


def aba_check(d: list):
    for a in d:
        if a[0] == "[":
            continue
        for i in range(len(a) - 2):
            if a[i] == a[i + 2] and not a[i] == a[i + 1]:
                if bab_check(d, a[i], a[i + 1]):
                    return True
    return False


def bab_check(d: list, A: chr, B: chr):
    for a in d:
        if not a[0] == "[":
            continue
        for i in range(1, len(a) - 2):
            if a[i] == B and a[i + 2] == B and a[i + 1] == A:
                return True
    return False


with open("input07") as file:
    data = file.read()
    print(count_ips(data))
    print(count_aba_ips(data))
