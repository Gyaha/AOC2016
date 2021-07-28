def read_data(data: str) -> list:
    d = []
    for l in data.splitlines():
        d.append(sorted([int(a) for a in l.split()]))
    return d


def count_legal_triangles(data: str) -> int:
    d = read_data(data)
    c = 0
    for t in d:
        if t[0] + t[1] > t[2]:
            c += 1
    return c


def read_data_2(data: str) -> list:
    l = [[int(a) for a in b.split()] for b in data.splitlines()]
    d = []
    for y in range(0, len(l), 3):
        for x in range(3):
            d.append(sorted([l[y][x], l[y + 1][x], l[y + 2][x]]))
    return d


def count_legal_triangles_2(data: str) -> int:
    d = read_data_2(data)
    c = 0
    for t in d:
        if t[0] + t[1] > t[2]:
            c += 1
    return c


with open("input03") as file:
    data = file.read()
    print(count_legal_triangles(data))
    print(count_legal_triangles_2(data))
