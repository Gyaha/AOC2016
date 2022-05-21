def read_data(data: str):
    d = []
    for l in data.splitlines():
        ll = l.split()
        d.append([int(ll[3]), int(ll[-1][:-1])])
    return d


def check_line(line):
    for l in line:
        if not l[1] == 0:
            return False
    return True


def align_line(line):
    for i, l in enumerate(line):
        l[1] += i
        while l[1] >= l[0]:
            l[1] -= l[0]


def add_line(line, x):
    for l in line:
        l[1] += x
        while l[1] >= l[0]:
            l[1] -= l[0]


def find_right_time(d: str):
    line = read_data(d)
    align_line(line)
    nudge = line[0][0] - line[0][1]
    add_line(line, nudge)
    n = nudge
    while not check_line(line):
        add_line(line, line[0][0])
        n += line[0][0]
    return n - line[0][0]


with open("input15") as f:
    d = f.read()
    print(find_right_time(d))
