def read_data(data: str) -> list:
    return [[a for a in b] for b in data.splitlines()]


def read_press(y, x) -> str:
    if y == 1:
        if x == -1:
            return "1"
        elif x == 0:
            return "2"
        else:
            return "3"
    elif y == 0:
        if x == -1:
            return "4"
        elif x == 0:
            return "5"
        else:
            return "6"
    else:  # == -1:
        if x == -1:
            return "7"
        elif x == 0:
            return "8"
        else:
            return "9"


def move_around_pad(y, x, i):  # -> int, int
    if i == "U":
        if y < 1:
            y += 1
    elif i == "R":
        if x < 1:
            x += 1
    elif i == "D":
        if y > -1:
            y -= 1
    else:  # == "L"
        if x > -1:
            x -= 1
    return y, x


def find_code(data: str) -> str:
    inst = read_data(data)
    y, x = 0, 0
    c = ""
    for l in inst:
        for ll in l:
            y, x = move_around_pad(y, x, ll)
        c += read_press(y, x)
    return c


def move_around_pad_2(y, x, i, pad):  # -> int, int
    ty, tx = y, x
    if i == "U":
        ty -= 1
    elif i == "R":
        tx += 1
    elif i == "D":
        ty += 1
    else:  # == "L"
        tx -= 1

    if is_inside_pad(ty, tx, pad):
        return ty, tx
    else:
        return y, x


def is_inside_pad(y, x, pad: list) -> bool:
    if y < 0 or y >= len(pad) or x < 0 or x >= len(pad[0]):
        return False
    return not pad[y][x] == " "


def read_press_2(y, x, pad):
    return pad[y][x]


def find_5(pad):  # -> int, int
    for y in range(len(pad)):
        for x in range(len(pad[0])):
            if pad[y][x] == "5":
                return y, x


def find_code_2(data: str, pad: list) -> str:
    inst = read_data(data)
    y, x = find_5(pad)
    c = ""
    for l in inst:
        for ll in l:
            y, x = move_around_pad_2(y, x, ll, pad)
        c += read_press_2(y, x, pad)
    return c


pad = ["  1  ",
       " 234 ",
       "56789",
       " ABC ",
       "  D  "]


with open("input02") as file:
    data = file.read()
    print(find_code(data))
    print(find_code_2(data, pad))
