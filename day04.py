import re
import string


def read_data(data: str) -> list:
    d = []
    for l in data.splitlines():
        d.append(re.split("([0-9]+)", re.sub("-|\[|\]", "", l)))
    return d


def find_rooms(data: str) -> int:
    d = read_data(data)
    n = 0
    for r in d:
        j = {}
        for c in string.ascii_lowercase:
            i = r[0].count(c)
            if i:
                if not i in j.keys():
                    j[i] = []
                j[i].append(c)
        c = ""
        for a in sorted(j.keys(), reverse=True):
            for b in sorted(j[a]):
                c += b
        if c[:5] == r[2]:
            n += int(r[1])
    return n


def find_shifted_room(data: str, search_word: str) -> int:
    d = read_data(data)
    o = ""
    for l in d:
        n = int(l[1])
        o = "".join([shift_letter(a, n) for a in l[0]])
        if search_word in o:
            return l[1]


def shift_letter(s: chr, n: int) -> chr:
    o = ord(s) - 97 + n
    while o >= 26:
        o -= 26
    return chr(o + 97)


with open("input04") as file:
    data = file.read()
    print(find_rooms(data))
    print(find_shifted_room(data, "northpoleobject"))
