def read_data(data: str):
    d = []
    for l in data.splitlines():
        d.append(l.split())
    return d


def get_val(a, b, c, d, t):
    if t == "a":
        return a
    elif t == "b":
        return b
    elif t == "c":
        return c
    elif t == "d":
        return d
    else:
        return int(t)


def set_val(a, b, c, d, t, v):
    if t == "a":
        a = v
    elif t == "b":
        b = v
    elif t == "c":
        c = v
    else:  # d
        d = v
    return a, b, c, d


def do_computer(a, b, c, d, data: str):
    data = read_data(data)
    i = 0
    while i < len(data):
        #print(i, a, b, c, d, data[i])
        if data[i][0] == "cpy":
            v = get_val(a, b, c, d, data[i][1])
            t = data[i][2]
            a, b, c, d = set_val(a, b, c, d, t, v)
            i += 1
        elif data[i][0] == "inc":
            v = get_val(a, b, c, d, data[i][1])
            t = data[i][1]
            a, b, c, d = set_val(a, b, c, d, t, v + 1)
            i += 1
        elif data[i][0] == "dec":
            v = get_val(a, b, c, d, data[i][1])
            t = data[i][1]
            a, b, c, d = set_val(a, b, c, d, t, v - 1)
            i += 1
        else:  # jnz
            t = get_val(a, b, c, d, data[i][1])
            v = get_val(a, b, c, d, data[i][2])
            if not t == 0:
                i += v
            else:
                i += 1

    return a


with open("input12") as f:
    d = f.read()
    print(do_computer(0, 0, 0, 0, d))
    print(do_computer(0, 0, 1, 0, d))
