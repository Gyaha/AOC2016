import string


def read_data(data: str):
    d = [[] for _ in range(len(data.splitlines()[0]))]
    for l in data.splitlines():
        for i, ll in enumerate(l):
            d[i].append(ll)
    return d


def find_code(data: str):
    d = read_data(data)
    code = ""
    for i in range(len(d)):
        h, ha = 0, ""
        for a in string.ascii_lowercase:
            c = d[i].count(a)
            if c > h:
                h = c
                ha = a
        code += ha
    return code


def find_code_2(data: str):
    d = read_data(data)
    code = ""
    for i in range(len(d)):
        h, ha = 99, ""
        for a in string.ascii_lowercase:
            c = d[i].count(a)
            if c < h:
                h = c
                ha = a
        code += ha
    return code


with open("input06") as file:
    data = file.read()
    print(find_code(data))
    print(find_code_2(data))
